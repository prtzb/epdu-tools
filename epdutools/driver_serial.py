# WORK IN PROGRESS

import os
import serial
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from epdutools.exceptions import ePDUException
from epdutools.validation import validate_partnumber, validate_serial, validate_version


class ePDU_serial(serial.Serial):

    def __init__(self, *args, **kwargs):
        super(ePDU_serial, self).__init__(*args, **kwargs)
        self.logged_in = False
        self.debug = False
        self.daisychain_amount = 0
    
    def login(self, user='admin', password='admin'):
        
        #self.logged_in = False
        self.user = user
        self.password = password
        self.open()
        
        while not self.logged_in:
            #line = self.readline().decode('utf-8')
            line = self.readline().decode('utf-8')
            
            if not line:
                self.write('\r'.encode('utf-8'))
            #else:
            #    print(line)

            if 'Enter Login:' in line:
                #self.__send_command(self.user)
                self.write(self.user.encode('utf-8'))
                continue
            elif 'Enter Password:' in line:
                #self.__send_command(self.password)
                self.write(self.password.encode('utf-8'))
                continue
            elif 'pdu#' in line:
                self.logged_in = True
        
        self.daisychain_amount = self.__get_daisychain_amount()
        self.info = self.__get_info_loop()
        self.mac_address = self.get_object('System.Ethernet.MacAddress')

    def logout(self):
        if self.logged_in:
            self.__send_command('quit')
        else:
            print('Not logged in.')

    def __send_command(self, cmd):
        
        send = str(cmd + '\r').encode('utf-8')
        self.write(send)
        self.readline()
        
        #reply = self.read(50)
        reply = self.readline().decode('utf-8').replace('\r', '').replace('\n', '')

        if self.debug:
            print(send)
            print(reply)
            #print('DEBUG (sent): ' + cmd)
            #print('DEBUG (reply): ' + reply)

        return reply

    def __get_daisychain_amount(self):
        #print('Checking for daishchain...')
        status = int(self.get_object('System.Daisychain.Status'))
        if status == 1:
            for nr in range(0,7):
                reply = self.__send_command('pdu ' + str(nr))
                if 'Error: The ePDU is not available' in reply:
                    self.daisychain_amount = nr
                    return nr
                #pos = int(self.get_object('System.Daisychain.DeviceID'))
                #if pos == 1:
                #    self.daisychain_amount = nr
                #    return nr
        else:
            self.daisychain_amount = 1
            return 1

    def __get_info_loop(self):
        
        result = []
        daisychain = self.daisychain_amount
        for i in range(0, daisychain):
            self.__send_command('pdu ' + str(i))
            info = self.__get_info()
            device_id = i
            info['DeviceID'] = device_id
            result.append(self.__get_info())
            #for option in objects:
            #    params[option] = pdu.get_object(option)
            #result.append(params)
            if daisychain > 1:
            #if daisychain > 1:
                self.__send_command('pdu ' + str(i + 1))
                daisychain -= 1
            else:
                return result
    
    def __get_info(self):
        objects = [
            'PDU.PowerSummary.iSerialNumber',
            'PDU.PowerSummary.iPartNumber',
            'PDU.PowerSummary.iVersion',
        ]
        params = {}
        for option in objects:
            params[option] = self.get_object(option)

        # Validations
        if not validate_version(params['PDU.PowerSummary.iVersion']):
            raise ePDUException('Validation Error: FW version ' + str(objects['PDU.PowerSummary.iVersion']))

        if not validate_serial(params['PDU.PowerSummary.iSerialNumber']):
            raise ePDUException('Validation Error: Serial Number ' + str(objects['PDU.PowerSummary.iSerialNumber']))

        if not validate_partnumber(params['PDU.PowerSummary.iPartNumber']):
            raise ePDUException('Validation Error: Part Number ' + str(objects['PDU.PowerSummary.iPartNumber']))
        
        return params
 
    def get_object(self, option):
        option = 'get ' + option
        return self.__send_command(option)

    def set_object(self, option, val):
        cmd = 'set ' + option + ' ' + val
        return self.__send_command(cmd)

    
