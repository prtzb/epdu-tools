import re

def validate_partnumber(pn):
    supported = [
        'EILB13',
        'EILB14',
        'EILB15',
        'EMIH28'
    ]
    if pn in supported:
        return True

def validate_serial(serial):
    try:
        return bool(re.match('[A-Z0-9]{10}', serial))
    except TypeError:
        return False

def validate_version(version):
    try:
        return bool(re.match('[0-9]{2}.[0-9]{2}.[0-9]{4}', version))
    except TypeError:
        return False

