# ePDU Tools


Python drivers for Eatons ePDU line.

Config parameters are stored in XML files on the unit. Both the http and the serial driver operates by reading and writing to these files. A table of the most common parameters can be found in the reference directory of this project.



## http
### Usage

To import:


    from epdutools.driver_http import ePDU


To inititialize a new object:


    pdu = ePDU('192.168.123.123', 'admin', 'admin', 5)


To receive basic info (such as serial number, product number, etc):

    
    >>> info = pdu.get_info()
    >>> import pprint
    >>> pprint.pprint(info)
    [{'Bootloader version': '00.00.0015',
    'Contact': '',
    'Contact Web Site': '<a target=_blank '
                        'href=http://www.eaton.com/epdu>http://www.eaton.com/ePDU</a>',
    'Description': 'ePDU INLINE METERED 0U/1.2U IN IEC309 32A 3P OUT 1xIEC309',
    'F/W version': '04.03.0001',
    'IPV4': '192.168.123.123',
    'IPV6': '',
    'Licenses': '/config/Open_Source_Licenses.txt?page=Open_Source_Licenses.txt',
    'Location': '',
    'Mac Address': '00:20:85:F4:36:7B',
    'Part Number': 'EILB15',
    'Serial Number': 'H715E49006',
    'Time Up': 2006326,
    'Web version': '0.0.0005'},
    {'F/W version': '04.03.0001',
    'Model': 'ePDU INLINE METERED 0U/1.2U IN IEC309 32A 3P OUT 1xIEC309',
    'Part Number': 'EILB15',
    'Serial Number': 'H715E49020'}]


To configure settings, pass a dict with the objects you want to change and their desired values:


    pdu.set_xml_object(
        {
            'System.Network.Hostname': 'my_pdu',
            'System.Network.SNMP.snmpVersion': '1',
            'System.Network.SNMP.V1.User[1].UserName': 'public'
        }  
    )


## Serial
### Usage


To import:

    from epdutools.driver_serial import ePDU_serial


To intitialize, specify the port appropriate for your OS. On Windows, it's usually something like "COM1". On Linux/OSX, specify the full path which is usually something like /dev/ttyUSB.


    pdu = ePDU_serial()
    pdu.baudrate = 9600
    pdu.port = 'COM3'
    pdu.timeout = 1
    # Set to True to enable debug output.
    # pdu.debug = True
    pdu.login()


To configure settings, the object and the desired value.


    pdu.set_object(
    	'System.Network.Hostname', 'my_pdu',
    )


**Note:** it's currently not possible to pass a dict so each object has to be passed on its own. The reason is that the ePDU does not natively support it. If multiple objects are to be changed, you can use a for loop:


    pdu_settings = {
        'System.Network.Hostname': 'my_pdu',
        'System.Network.DHCP': '0',
        'System.Network.IPAddress': '10.0.1.10,
        'System.Network.IPMask': '255.255.255.0',
        'System.Network.IPGateway': '10.0.1.1',
        'System.Network.SNMP.snmpVersion': '1',
        'System.Network.SNMP.V1.User[1].UserName': 'my_C0munity',
        'System.Network.SNMP.V1.User[1].SecurityRight': '1',
        'System.Restart': '1',
    }

    for k, v in pdu_settings.items():
        print('* Setting ', k, 'to ', v)
        pdu.set_object(k, v)
