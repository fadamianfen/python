import configparser
import os,sys,re

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        print(configpath)
        remove_BOM(configpath)
        self.cf.read(configpath,encoding='UTF-8')

    def get_db(self, confstr,param):
        value = self.cf.get(confstr, param)
        return value

def remove_BOM(config_path):  # 去掉配置文件开头的BOM字节
    content = open(config_path, encoding='UTF-8').read()
    # Window下用记事本打开配置文件并修改保存后，编码为UNICODE或UTF-8的文件的文件头
    # 会被相应的加上\xff\xfe（\xff\xfe）或\xef\xbb\xbf，然后再传递给ConfigParser解析的时候会出错
    # ，因此解析之前，先替换掉
    content = re.sub(r"\ufeff", "", content)
    content = re.sub(r"\xfe\xff", "", content)
    content = re.sub(r"\xff\xfe", "", content)
    content = re.sub(r"\xef\xbb\xbf", "", content)
    print(content)
    open(config_path,"r+", encoding='UTF-8').write(content)
