"""
ePDU Tools

This is a driver for Eaton's ePDU line. 
by Staffan Linnaeus 2020

"""

import base64
import hashlib
import json
import logging
import os
import re
import requests
from requests.auth import HTTPBasicAuth
import sys
import time
import urllib
from urllib.parse import urlencode, quote
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from epdutools.exceptions import ePDUException

def _dc():
    """Simple timestamp added to every URL"""
    dc = str(int(time.time() * 1000))
    return dc

def generate_nc(val):
    """This function is used for authentication."""
    # The server always gives the same value ("1") so this always returns "000000001"
    # This can probably be replaced by ha hardcoded value but since the original code does this for some reason, I'll leave it here.
    while len(val) < 8:
        val = "0" + val
    return val

def generate_sessionKey(user, pw, data):
    """This function is used for authentication."""
    
    # These variable names are all taken from the original code.
    szUsername = user
    passwordUser = pw
    szRealm = data[0]
    szNonce = data[1]
    szCnonce = data[2]
    
    # Also from the original code. I'll leave them in case I should need them later.
    # szUri = data[3]
    # szQop = data[4]
    # uiNcValue = data[5] + ""
    # loginChallenge = szUsername.encode('utf8')
    # passwordChallenge = passwordUser.encode('utf8')
    # szRealmChallenge = szRealm.encode('utf8')

    a = szUsername + ':' + szRealm + ':' + passwordUser
    a = a.encode('utf8')
    a = hashlib.md5(a).digest()
    b = ':' + szNonce + ':' + szCnonce
    b = b.encode('utf8')
    c = a + b
    sessionKey = hashlib.md5(c)

    return sessionKey

def generate_szResponse(data, sessionKey):
    """This function is used for authentication"""
    szNonce = data[1]
    szCnonce = data[2]
    szUri = data[3]
    szQop = data[4]
    uiNcValue = data[5] + ""
    nc_val = generate_nc(uiNcValue)
    s2Client = "AUTHENTICATE:" + szUri
    s2Client = hashlib.md5(bytes(s2Client.encode('utf8')))
    a = sessionKey.hexdigest()
    b = ":" + szNonce + ":" + nc_val + ":" + szCnonce + ":" + szQop + ":"
    c = s2Client.hexdigest()
    d = a + b + c
    d = bytes(d.encode('utf8'))
    szResponse = hashlib.md5(d)
    return szResponse

def generate_szResponseValue(data, sessionKey):
    """This function is used for authentication"""
    szNonce = data[1]
    szCnonce = data[2]
    szUri = data[3]
    szQop = data[4]
    uiNcValue = data[5] + ""
    nc_val = generate_nc(uiNcValue)
    s2Server = ":" + szUri
    s2Server = hashlib.md5(bytes(s2Server.encode('utf8')))
    a = sessionKey.hexdigest()
    b = ":" + szNonce + ":" + nc_val + ":" + szCnonce + ":" + szQop + ":"
    c = s2Server.hexdigest()
    d = a + b + c
    d = bytes(d.encode('utf8'))
    szResponseValue = hashlib.md5(d)
    return szResponseValue

def is_success(data):
    """ Parses JSON response for success string """
    if data['success'] == "true":
        return True
    else:
        return False

def parse_info(data):
    """ Parses ePDU info to dict, which is more readable."""
    if is_success(data):
        result = []
        for i in data['data']:
            result.append(list_to_dict(i))
        return result
    else:
        return print("Error! Data: " + str(data['error']))

def list_to_dict(data):
    """ Converts specific list object to dictionary """
    result = {}
    for row in data:
        result[row[0]] = row[1]
    return result

def parse_data(data):
    """ Fixes broken JSON formatting """
    replace = {
        '"' : '', 
        'success' : '"success"',
        'true':'"true"',
        'data':'"data"',
        'status':'"status"',
        'error':'"error"',
        '\[,,\]':'[0,0]',
        "'":'"'
    }
    for k,v in replace.items():
        data = re.sub(k,v, data)
    dump = json.loads(data)
    return dump

def parse_readings(data):
    """ This is to create a more readable dict from the rather messy JSON """
    data = data['data'][4][0]
    result = list_to_dict(data[8]) 
    for phase in range(0,len(data[2])):
        phase_dict = {   
            'label': data[2][phase],
            'amps': data[3][phase][1],
            'amps_total':data[3][phase][5],
            'voltage':data[4][phase][1]
        }
        result[data[2][phase]] = phase_dict
    return result

def parse_challenge(response, version):
    """ This functions exists only because the challenge data format changed between v1 and v2. """
    if version <= 1000031:
        response['data'].pop(1)
        response['data'][6].pop(0)
    return response

def find_fw_version(host):
    """ Gets the fw version from the login splash page """
    url_part = '/config/gateway?page=cgi_webAndFirmware_information'
    url = 'http://' + host + url_part
    req = requests.get(url)
    parsed = parse_data(req.text)
    find_list = find_list_in_list(parsed['data'])
    fw_version = int(find_list[1][1].replace('.', ''))
    return fw_version

def find_list_in_list(mylist):
    """ Helper function for find_fw_version """
    for i in mylist:
        if type(i) is list:
            return i
    return None
        
class ePDU:
    
    def __init__(self, host, user, pw, timeout):
    
        """ The ePDU object.

            :param host: ip/hostname
            :param user: username
            :param password: password
            :param timeout: timeout in seconds

        """    

        self.error_codes = { 
            3338 : "Wrong credentials.",
            3334 : "Too many active sessions.",
            3337 : "Permission error."
        }
        self.is_auth = False
        self.timeout = timeout
        self.ip = host
        self.host = "http://" + self.ip + "/"
        self.gw = "config/gateway?"
        self.url_gw = self.host + self.gw
        self.url_config = self.host + "config/"
        self.common_url_headers = { 
            'Host':             self.ip,
            'Connection':       'keep-alive',
            'User-Agent':       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer':          self.host,
            'Accept-Encoding':  'gzip, deflate',
            'Accept-Language':  'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7' 
        }

        # FIND FIRMWARE VERSION
        self.fw_version = 2000001
        try:
            self.fw_version = find_fw_version(self.ip)
        except requests.exceptions.ConnectionError:
            raise ePDUException("Host not responding.")
        user_b64 = base64.b64encode(user.encode('utf8')).decode('utf8')
        if self.fw_version > 1000031:
            self.user_url = user_b64
        else:
            self.user_url = user
        
        # AUTHENTICATION
        # 1. Prepare and send URL with base64-encoded username included.

        auth_url_vars = self._add_url_parameters([  
                            ('page', 'cgi_authentication'),
                            ('login', self.user_url),
                            ('_dc', _dc())],
                        )
        try:
            response = self.__send_get_request(auth_url_vars)
        except requests.exceptions.ConnectionError:
            raise ePDUException("Host not responding.")
        
        # 2. Server Response should include a sessionId, two nonces and some other values.
        # Response format is malformed so we have to parse it manually. 
        # All of these are used to create 3 md5 hashes.
        # Finally, these hashes are sent to the server included in a new URL that we generate.
        response_parsed = parse_challenge(parse_data(response.text), self.fw_version)
        self.sessionId = response_parsed['data'][0]
        self.data = response_parsed['data'][6]

        challenge_url_vars = self._add_url_parameters([ 
            ('page','cgi_authenticationChallenge'),
            ('sessionId', self.sessionId),
            ('login', self.user_url),
            ('sessionKey', generate_sessionKey(user, pw, self.data).hexdigest()),
            ('szResponse', generate_szResponse(self.data, generate_sessionKey(user, pw, self.data)).hexdigest()),
            ('szResponseValue', generate_szResponseValue(self.data, generate_sessionKey(user, pw, self.data)).hexdigest()),
            ('_dc', _dc())
        ])

        try:
            challenge_details = self.__send_get_request(challenge_url_vars)
        except requests.exceptions.ConnectionError:
            raise ePDUException("Host not responding.")

        # 3. Check response for status code.
        status = parse_data(challenge_details.text)
        if "status" in status.keys():       
            status_code = status['status']
        elif "error" in status.keys():
            status_code = status['error']
        if status_code == 0:
            #print("Login successful.")
            self.is_auth = True
        else:
            print(challenge_details.text)
            raise ePDUException(str(status_code) + ": " + self.error_codes[status_code])
            
        # 4. Verify session.
        self.cookie = { 
            'sessionID':    self.sessionId, 
            'credential':   urllib.parse.quote(self.sessionId + "," + user + "1" + "," + "0" + "," + "2" + "," + "0"),
        }

        check_session_url_vars = self._add_url_parameters([ 
            ('page', 'cgi_checkUserSession'),
            ('sessionId', self.sessionId),
            ('_dc', _dc())
        ])

        check_session = self.__send_get_request(check_session_url_vars, self.cookie)
        
        # AUTHENTICATION COMPLETE!
        
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """ Uses the .close() method to logout and close the session. """
        self.close()
        return True

    def __send_get_request(self, url_parameters, *args):
        """ Crafts URL and sends request. """
        url = self.url_gw + urllib.parse.urlencode(
            url_parameters, 
            quote_via=quote)
        if args:
            cookie = args[0]
            response = requests.get(
                url, 
                cookies=cookie, 
                timeout=self.timeout)
        else:
            response = requests.get(url, timeout=self.timeout)
        return response

    def _add_url_parameters(self, url_parameters):
        """ Determine the order of the parameters in the URL """

        if self.fw_version <= 1000031 and ('login', self.user_url) not in url_parameters:
            pos = [x for x, y in enumerate(url_parameters) if y[0] == 'page']
            if not pos:
                pos = 0
            else:
                pos = pos[0]+1
            url_parameters.insert(pos, ('login', self.user_url))
        return url_parameters

    def close(self):
        """
        This method handles the logout process. Always remember to use this, 
        as the ePDU can only hold a very limited amount of sessions.
        """
        logout_url_vars = self._add_url_parameters([ 
            ('page', 'cgi_logout'),
            ('sessionId', self.sessionId),
            ('_dc', _dc())]
            )
        logout = self.__send_get_request(logout_url_vars, self.cookie)
        if logout.text == "{success:true}":
            return True
        else:
            return False

    def set_xml_object(self, obj):
        """
        Accepts a dict with valid settings and their desired values.
        This is formated into an XML request and sent to the server.
        This is used as a basis for any other function that configures a specific setting.
        """
        xml_set_object = ET.Element("SET_OBJECT")
        for k,v in obj.items():
            ET.SubElement(xml_set_object, "OBJECT", name=k).text = v
        tree = ET.ElementTree(xml_set_object)
        xml_string = ET.tostring(tree.getroot())
        set_obj_url_vars = self._add_url_parameters([  
            ('sessionId', self.sessionId),
            ('_dc', _dc())  
            ]
        )
        set_obj_headers = self.common_url_headers
        set_obj_headers.update(
            {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})
        set_obj_url = self.url_config + "set_object.xml?" + urllib.parse.urlencode(set_obj_url_vars, quote_via=quote)
        response = requests.post(
            set_obj_url, 
            cookies=self.cookie, 
            headers=set_obj_headers, 
            data=xml_string, 
            timeout=self.timeout
        )
        tree = ET.fromstring(response.text)
        return tree

    def set_snmp_community(self, community, version):
        """ Enables SNMP and sets community """
        params = {  
            'System.Network.SNMP.snmpVersion':          version, 
            'System.Network.SNMP.V1.User[1].UserName':  community 
        }
        response = self.set_xml_object(params)
        return response

    def set_ip(self, ip, subnet, gw):
        """ Disables DHCP and sets a new IP """
        params = {  
            'System.Network.DHCP':      "0",
            'System.Network.IPAddress': ip,
            'System.Network.IPMask':    subnet,
            'System.Network.IPGateway': gw
        }
        response = self.set_xml_object(params)
        self.restart()
        return response

    def firmware_update(self, file, progress_bar=False):
        """ This is built on Request's file upload feature. Just pass a valid .bin file. """
        my_file = {'file': open(file, 'rb')}
        
        fw_url_vars = [
            ('sessionID', self.sessionId)
        ]

        if self.fw_version < 1000034:
            fw_url_vars.insert(0, ('login', self.user_url))
        
        fw_url = self.url_config + "image.bin?" + urllib.parse.urlencode(fw_url_vars, quote_via=quote)
        response = requests.post(
            fw_url, 
            cookies=self.cookie, 
            files=my_file)
        return response

    def factory_reset(self):
        """ Erases all config and reverts back to factory settings. Use with caution! """
        response = self.set_xml_object({'System.FactoryReset':'1'})
        return response

    def restart(self):
        """ Restarts ePDU management without distrupting power supply """
        response = self.set_xml_object({'System.Restart': '1'})
        return response

    def get_readings(self, index_pdu=0):
        """ Returns dict with reading for given unit """
        readings_url_vars = self._add_url_parameters([ 
            ('page','cgi_overview'),
            ('sessionId', self.sessionId),
            ('index_pdu', index_pdu),
            ('_dc', _dc())
            ]
        )
        readings = self.__send_get_request(readings_url_vars, self.cookie)
        result = parse_readings(parse_data(readings.text))
        return result

    def get_info(self):
        """ 
        Returns list of dicts with basic info such as serial number and mac adress.
        Each item on the list is a daisychained pdu.
        """
        info_url_vars = self._add_url_parameters([ 
            ('page', 'cgi_pdu_information'),
            ('sessionId', self.sessionId),
            ('_dc', _dc())
        ])
        info = self.__send_get_request(info_url_vars, self.cookie)
        info_parsed = parse_info(parse_data(info.text))
        return info_parsed

class ePDU_G1:
    def __init__(self, host, user, pw, timeout):
        self.host = host
        self.timeout = timeout
        self.user = user
        self.pw = pw

    def get_info(self):
        """Returns a dict with basic info about the device."""
        response = requests.get(
            'http://' + self.host + '/ws/properties.xml', 
            auth=(self.user, self.pw), 
            timeout=self.timeout
        )
        tree = ET.fromstring(response.content)
        pdu_info = {}
        for i in tree:
            attribute = i.attrib['name']
            text = i.text
            pdu_info[attribute] = text
        return pdu_info

    def set_xml_object(self, obj):
            """
            EXPERIMENTAL! USE WITH CAUTION!
            Accepts a dict with valid settings and their desired values.
            This is formated into an XML request and sent to the server.
            This is used as a basis for any other function that configures a specific setting.
            """
            xml_set_object = ET.Element("SET_OBJECT")
            for k,v in obj.items():
                ET.SubElement(xml_set_object, "OBJECT", name=k).text = v
            tree = ET.ElementTree(xml_set_object)
            xml_string = ET.tostring(tree.getroot())
            headers = { 'Content-Type':'application/xml' }
            url = 'http://' + self.host + '/ws/properties.xml'  
            try:
                requests.post(
                    url, 
                    auth=(self.user, self.pw),
                    headers=headers,
                    data=xml_string, 
                    timeout=self.timeout
                )
            except requests.exceptions.ConnectionError:
                # This super ugly hack is needed because the G1 pdus do not send a response,
                # even on a successful post.
                return True
