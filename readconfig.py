import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.realpath(__file__))
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        print(configpath)
        self.cf.read(configpath,encoding='utf-8')

    def get_db(self, confstr,param):
        value = self.cf.get(confstr, param)
        return value
