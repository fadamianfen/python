import sys

from PyQt5 import QtWidgets

from peimaiqi import readconfig, shujuku
from PyQt5.QtWidgets import QApplication, QMainWindow
from peimaiqi.untitled import Ui_MainWindow
import peimaiqi.crcmodbus as crc
from peimaiqi.baojing import *
from peimaiqi.chuankou import *

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
    def qidong1(self):  # 1号秤启动
        try:
            if (ser.is_open):
                str = '0105000dff001df9'  # 1号秤启动命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                print(STRGL)
                if STRGL.__eq__(str):
                    mywin.label_34.setText("启动成功")
                else:
                    mywin.label_34.setText("启动失败")
        except Exception as e:
            print(e)
            mywin.label_34.setText("启动失败")
    def qidong2(self):  #
        try:
            if (ser.is_open):
                str = '0205000dff001dca'  # 2#秤启动命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                print(STRGL)
                if STRGL.__eq__(str):
                    mywin.label_36.setText("启动成功")
                else:
                    mywin.label_36.setText("启动失败")
        except Exception as e:
            print(e)
            mywin.label_36.setText("启动失败")
    def qidong3(self):  #3号秤启动
        try:
            if (ser.is_open):
                str = '0205000dff001c1b'  # 3#秤启动命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                print(STRGL)
                if STRGL.__eq__(str):
                    mywin.label_38.setText("启动成功")
                else:
                    mywin.label_38.setText("启动失败")
        except Exception as e:
            print(e)
            mywin.label_38.setText("启动失败")
    def tingzhi1(self):  #1号秤停止
        try:
            if (ser.is_open):
                str = '0105000d00005c09'  # 1号秤停止命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                if STRGL.__eq__(str):
                    mywin.label_34.setText("停止成功")
                else:
                    mywin.label_34.setText("停止失败")
        except Exception as e:
            print(e)
            mywin.label_34.setText("停止失败")
    def tingzhi2(self):  #2号秤停止
        try:
            if (ser.is_open):
                str = '0205000d00005c3a'#2号秤停止命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                if STRGL.__eq__(str):
                    mywin.label_36.setText("停止成功")
                else:
                    mywin.label_36.setText("停止失败")
        except Exception as e:
            print(e)
            mywin.label_36.setText("停止失败")
    def tingzhi3(self):  # 3号秤停止
        try:
            if (ser.is_open):
                str = '0105000d00005deb'  # 3号秤停止命令
                DWritePort(ser, str)
                #time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                if STRGL.__eq__(str):
                    mywin.label_38.setText("停止成功")
                else:
                    mywin.label_38.setText("停止失败")
        except Exception as e:
            print(e)
            mywin.label_38.setText("停止失败")
    def shezhi1(self):  #1号秤设置目标流量
        if crc.is_number(mywin.lineEdit.text().strip()):
            st = crc.float_to_hex(float(mywin.lineEdit.text().strip()))#浮点数转十六进制
            st1=str(crc.crc16Add(str7+st)).replace(' ','')#返回带校验位的十六进命令串
            try:
                if (ser.is_open):
                    DWritePort(ser, st1)
                    #time.sleep(0.5)
                    STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                    if STRGL.__eq__('01100000000241c8'):
                        mywin.label_34.setText("设置成功")
                        #刷新一下目标流量前端显示
                        mywin.label_11.setText(mywin.lineEdit.text().strip())  # 目标流量

                    else:
                        mywin.label_34.setText("设置失败")
            except Exception as e:
                print(e)
                mywin.label_34.setText("设置失败")
    def shezhi2(self):  #2号秤设置目标流量
        if crc.is_number(mywin.lineEdit_2.text().strip()):
            st = crc.float_to_hex(float(mywin.lineEdit_2.text().strip()))  # 浮点数转十六进制
            st1 = str(crc.crc16Add(str7 + st)).replace(' ', '')  # 返回带校验位的十六进命令串
            try:
                if (ser.is_open):
                    DWritePort(ser, st1)
                    #time.sleep(0.5)
                    STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                    if STRGL.__eq__('02100000000241fb'):
                        mywin.label_36.setText("设置成功")
                        # 刷新一下目标流量前端显示
                        mywin.label_15.setText(mywin.lineEdit_2.text().strip())  # 更新目标流量

                    else:
                        mywin.label_36.setText("设置失败")
            except Exception as e:
                print(e)
                mywin.label_36.setText("设置失败")
    def shezhi3(self):  #3号秤设置目标流量
        if crc.is_number(mywin.lineEdit_3.text().strip()):
            st = crc.float_to_hex(float(mywin.lineEdit_3.text().strip()))  # 浮点数转十六进制
            st1 = str(crc.crc16Add(str7 + st)).replace(' ', '')  # 返回带校验位的十六进命令串
            try:
                if (ser.is_open):
                    DWritePort(ser, st1)
                    #time.sleep(0.1)
                    STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                    if STRGL.__eq__('031000000002402a'):
                        mywin.label_38.setText("设置成功")
                        # 刷新一下目标流量前端显示
                        mywin.label_27.setText(mywin.lineEdit_3.text().strip())  # 更新目标流量

                    else:
                        mywin.label_38.setText("设置失败")
            except Exception as e:
                print(e)
                mywin.label_38.setText("设置失败")
    def qingbaojing(self):#1号秤清报警
        try:
            if (ser.is_open):
                str = '0105000eff00edf9'  # 清除1号秤报警，2号秤0205000eff00edca，3号秤0305000eff00ec1b
                DWritePort(ser, str)
                time.sleep(0.5)
                STRGL = str(binascii.b2a_hex(ser.readline()))[2:-1]
                print(STRGL)
                if STRGL.__eq__(str):
                    mywin.label_34.setText("清除成功")
                else:
                    mywin.label_34.setText("清除失败")
        except Exception as e:
            print(e)
            mywin.label_34.setText("清除失败")
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
import threading, datetime, time, struct, binascii

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
        hour = time.localtime().tm_hour
        now = datetime.datetime.now()
        if (ser.is_open):
            #1号秤信息
            mubiao1=readserial(ser,'010300000002C40B')#读取1号秤目标流量
            mywin.label_11.setText(str(mubiao1))#显示1号秤目标流量
            leiji1=readserial(ser,'01030008000245C9')#读取1号秤累计流量
            mywin.label_3.setText(str(leiji1))  # 显示1号秤累计流量
            shunshi1=readserial(ser,'0103000A0002E409')#读取1号瞬时计流量
            mywin.label_5.setText(str(shunshi1))  # 显示1号秤瞬时流量
            DWritePort(ser, '010400100002700')  # 读取状态
            zhuangtai1 = str(binascii.b2a_hex(ser.readline()))[11:12]
            mywin.label_34.setText(baojing(zhuangtai1))  # 调用baojing.py中的报警信息处理函数，并返回值。


'''
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
            mywin.label_34.setText(baojing(STRGLO3))#调用baojing.py中的报警信息处理函数，并返回值。
            '''
            try:
                s = "INSERT INTO liuliang VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')"
                sqlstr=s.format('一厂区三车间',班组,now.strftime("%Y-%m-%d"),now.strftime("%H:%M:%S"),STRGLO1[0:2],flnum,flnum1,0)
                if not STRGLO3.__eq__('5'):#只要不是停止运行就写数据库。
                    shujuku.sqlzsg(sqlstr)
                    print('写数据库')
            except Exception as e:
                print(e)
                mywin.label_3.setText('数据异常！')#累计流量
                mywin.label_5.setText('数据异常！')#瞬时流量
        time.sleep(60)


str1 = '010300000002C40B'  # 读取目标流量命令
str2 = '01030008000245C9'  # 读取累计流量
str3 = '0103000A0002E409'  # 读取瞬时流量
str4 = '010400100002700E' #读取状态
str7 = '01100000000204'    # 设置目标流量命令的前面部分，+数据位+校验位即是完整命令。

if __name__ == "__main__":
    readcon= readconfig.ReadConfig()#实例化读配置文件类。
    port=readcon.get_db('serial','串口')
    betelv=readcon.get_db('serial','波特率')
    app = QApplication(sys.argv)
    mywin = Mymainform()
    mywin.show()
    ser, ret = DOpenPort(port, betelv)
    if (ser.is_open):
        threading.Thread(target=ReadData, args=(ser,)).start()
    sys.exit(app.exec_())
