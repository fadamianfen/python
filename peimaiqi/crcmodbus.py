from binascii import *
from crcmod import *
import struct


# CRC16-MODBUS
def crc16Add(read):
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    data = read.replace(" ", "")
    readcrcout = hex(crc16(unhexlify(data))).upper()
    str_list = list(readcrcout)
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0
    crc_data = "".join(str_list)
    print(crc_data)
    read = read.strip() + ' ' + crc_data[4:] + ' ' + crc_data[2:4]
    print('CRC16校验:', crc_data[4:] + ' ' + crc_data[2:4])
    print('增加Modbus CRC16校验：>>>', read)
    return read


def float_to_hex(f):
    s=hex(struct.unpack('<I', struct.pack('<f', f))[0])
    h=s[6:]+s[2:6]
    return h


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
