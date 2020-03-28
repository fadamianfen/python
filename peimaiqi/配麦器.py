import sys

from PyQt5 import QtWidgets

from peimaiqi import readconfig, shujuku
from PyQt5.QtWidgets import QApplication, QMainWindow
from peimaiqi.untitled import Ui_MainWindow
import peimaiqi.crcmodbus as crc

class Mymainform(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mymainform, self).__init__()
        self.setupUi(self)
        # self.login_Button.clicked.connect(self.display)
        # self.pushButton.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        # self.cancel_Button.clicked.connect(self.close)
        # self.pushButton_2.clicked.connect(self.close)
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "不允许退出程序",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.ignore()
            #event.accept()
        else:
            event.ignore()
    def qidong1(self):  #
        try:
            if (ser.is_open):
                DWritePort(ser, str5)
                time.sleep(0.5)
                STRGLO5 = str(binascii.b2a_hex(ser.readline()))[2:-1]
                print(STRGLO5)
                if STRGLO5.__eq__(str5):
                    mywin.label_34.setText("启动成功")
                else:
                    mywin.label_34.setText("启动失败")
        except Exception as e:
            print(e)
            mywin.label_34.setText("启动失败")
    def qidong2(self):  #
        pass
    def qidong3(self):  #
        pass
    def tingzhi1(self):  #
        try:
            if (ser.is_open):
                DWritePort(ser, str6)
                time.sleep(0.5)
                STRGLO6 = str(binascii.b2a_hex(ser.readline()))[2:-1]
                if STRGLO6.__eq__(str6):
                    mywin.label_34.setText("停止成功")
                else:
                    mywin.label_34.setText("停止失败")
        except Exception as e:
            print(e)
            mywin.label_34.setText("停止失败")
    def tingzhi2(self):  #
        pass
    def tingzhi3(self):  #
        pass
    def shezhi1(self):  #
        if crc.is_number(mywin.lineEdit.text().strip()):
            st = crc.float_to_hex(float(mywin.lineEdit.text().strip()))
            st1=str(crc.crc16Add(str7+st)).replace(' ','')
            try:
                if (ser.is_open):
                    DWritePort(ser, st1)
                    time.sleep(0.5)
                    STRGLO7 = str(binascii.b2a_hex(ser.readline()))[2:-1]
                    if STRGLO7.__eq__('031000000002402a'):
                        mywin.label_34.setText("设置成功")
                        #刷新一下目标流量前端显示
                        mywin.label_11.setText(mywin.lineEdit.text().strip())  # 目标流量

                    else:
                        mywin.label_34.setText("设置失败")
            except Exception as e:
                print(e)
                mywin.label_34.setText("设置失败")

    def shezhi2(self):  #
        pass
    def shezhi3(self):  #
        pass
    def yuebaobiao(self):  #
        pass
    def banzubaobiao(self):  #
        pass
    def ribaobiao(self):  #
        pass
    def guanyu(self):  #
        pass
    def bangzhu(self):  #
        pass
    def banzushezhi(self):  #
        pass

# 串口模块区域
import serial, threading, datetime, time, struct, binascii
import serial.tools.list_ports


STRGLO = ""  # 读取的累计流量
STRGLO1 = ""  # 读取的瞬时流量
STRGLO2 = ""  # 读取的目标流量
STRGLO3 = ""  #读取状态
BOOL = True  # 读取标志位
# 读数代码本体实现
def ReadData(ser):
    global STRGLO,STRGLO1,STRGLO2,BOOL,dakai
    # 循环接收数据，此为死循环，可用线程实现
    while BOOL:# and dakai is True:
        mon = time.localtime().tm_mon
        day = time.localtime().tm_mday
        hour = time.localtime().tm_hour
        min = time.localtime().tm_min
        now = datetime.datetime.now()
        # 转换为指定的格式:
        styleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        if (ser.is_open):

            DWritePort(ser, str1)#读取目标流量
            time.sleep(1)
            STRGLO2 = str(binascii.b2a_hex(ser.readline()))[2:-1]

            DWritePort(ser, str2)#读取累计流量
            time.sleep(1)
            STRGLO = str(binascii.b2a_hex(ser.readline()))[2:-1]

            DWritePort(ser, str3)#读取瞬时流量
            time.sleep(1)
            STRGLO1 = str(binascii.b2a_hex(ser.readline()))[2:-1]
            print(STRGLO1)

            DWritePort(ser, str4)#读取状态
            time.sleep(1)
            STRGLO3 = str(binascii.b2a_hex(ser.readline()))[11:12]
            print(STRGLO3)
            if STRGLO3.__eq__('6'):
                mywin.label_34.setText("正常运行")
            elif STRGLO3.__eq__('5'):
                mywin.label_34.setText("停止运行")
            elif STRGLO3.__eq__('4'):
                mywin.label_34.setText("卡料报警")
            elif STRGLO3.__eq__('3'):
                mywin.label_34.setText("超量程报警")
            elif STRGLO3.__eq__('2'):
                mywin.label_34.setText("电压超限报警")
            else:
                mywin.label_34.setText("空料报警")

            try:
                flnum2 = round(struct.unpack('!f', bytes.fromhex(STRGLO2[10:14] + STRGLO2[6:10]))[0],2)
                mywin.label_11.setText(str(flnum2))  # 目标流量
                flnum = round(struct.unpack('!f', bytes.fromhex(STRGLO[10:14] + STRGLO[6:10]))[0], 4)
                mywin.label_3.setText(str(flnum))#累计流量
                if hour>=7 and hour<19:
                    班组='白班'
                else:
                    班组='夜班'
                flnum1 = round(struct.unpack('!f', bytes.fromhex(STRGLO1[10:14] + STRGLO1[6:10]))[0],4)
                mywin.label_5.setText(str(flnum1))#瞬时流量
                s = "INSERT INTO liuliang VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')"
                sqlstr=s.format('聊城公司',班组,now.strftime("%Y-%m-%d"),now.strftime("%H:%M:%S"),STRGLO1[0:2],flnum,flnum1,0)
                if not STRGLO3.__eq__('5'):
                    shujuku.sqlzsg(sqlstr)
                    print('写数据库')

            except Exception as e:
                print(e)
                mywin.label_3.setText('数据异常！')#累计流量
                mywin.label_5.setText('数据异常！')#瞬时流量
        time.sleep(60)

# 打开串口
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
def DOpenPort(portx, bps):
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=0.5)
        ser.bytesize = 8  # 可有可无
        ser.parity = 'N'  # 可有可无
        ser.stopbits = 1  # 可有可无
        # 判断是否打开成功
        if (ser.is_open):
            ret = True
            threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        mywin.label_34.setText('线程异常！')
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


str1 = '030300000002C5E9'  # 读取目标流量命令
str2 = '030300080002442B'  # 读取累计流量
str3 = '0303000A0002E5EB'  # 读取瞬时流量
str4 = '03040010000271EC'  # 读取状态

str5 = '0305000dff001c1b'  # 启动
str6 = '0305000d00005deb'  # 停止
str7 = '03100000000204'    # 设置目标流量命令的前面部分，+数据位+校验位即是完整命令。

if __name__ == "__main__":
    readcon= readconfig.ReadConfig()#实例化读配置文件类。
    port=readcon.get_db('serial','串口')
    betelv=readcon.get_db('serial','波特率')
    app = QApplication(sys.argv)
    mywin = Mymainform()
    mywin.show()
    ser, ret = DOpenPort(port, betelv)
    sys.exit(app.exec_())