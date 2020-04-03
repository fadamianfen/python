#16位modbus校验位计算；
#浮点数转十六进制；
#判断输入的是否是数字；
from binascii import *
import crcmod
import struct


# CRC16-MODBUS 计算十六进制命令的校验位的，返回的是已经带命令+校验位的字符串了。
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

#浮点数转十六进制，比如10.0转十六进制为0x41200000，其中0x没用需要去除一下。
def float_to_hex(f):
    s=hex(struct.unpack('<I', struct.pack('<f', f))[0])
    h=s[6:]+s[2:6]#发给硬件设备的命令是低位在前，所以要倒一下。
    return h

#判断输入的字符串是不是数字的函数，如果是数字返回Ture否则返回False
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
