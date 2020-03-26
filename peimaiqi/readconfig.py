import configparser
import os,sys,re

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        configpath = os.path.join(root_dir, "config.cfg")
        self.cf = configparser.ConfigParser()
        print(configpath)
        self.cf.read(configpath,encoding='UTF-8-sig')
        #这里存在的问题是windows编辑配置文件保存后，会在文件前面加上‘\ufeff’,造成文件read失败，编码必须使用UTF-8-sig才行。

    def get_db(self, confstr,param):
        value = self.cf.get(confstr, param)
        return value

