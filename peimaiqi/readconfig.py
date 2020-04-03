#读配置文件的类，最终程序打包完成后要将配置文件config.cfg放在程序根目录下。配置文件格式如下：
#[section1]
#a=1
#b=2
#[section2]
#c=3
#b=4
#使用该文件的方法为：引入该文件import readconfig 然后实例化类对象，比如readconf=ReadConfig()  然后调用类中的函数
# readconf.get_db(confstr,param)函数获取config.cfg中的内容。
#函数中的两个参数分别是配置文件中的section和该section下面的健。函数返回的是该健的value。
#比如 readconf.get_db("section1","b")返回的是2，注意参数要用单引号或双引号引起来。
import configparser
import os,sys

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