# 打开串口
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
from serial import Serial
from binascii import b2a_hex
from struct import unpack
def DOpenPort(portx, bps):
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = Serial(portx, bps, timeout=0.5)
        ser.bytesize = 8  # 可有可无
        ser.parity = 'N'  # 可有可无
        ser.stopbits = 1  # 可有可无
        # 判断是否打开成功
        if (ser.is_open):
            ret = True
    except Exception as e:
        print(e)
    return ser, ret

# 关闭串口
def DColsePort(ser):
    global BOOL
    BOOL = False
    ser.close()

# 写数据
def DWritePort(ser, text):
    result = ser.write(bytes.fromhex(text))  # 写数据
    return result
#在主函数中调用，用于返回读取到的浮点数值。
def readserial(ser,str):
    if (ser.is_open):
        DWritePort(ser, str)
        STRGL = str(b2a_hex(ser.readline()))[2:-1]
        flnum = round(unpack('!f', bytes.fromhex(STRGL[10:14] + STRGL[6:10]))[0], 2)
        return flnum
    else:
        return None
