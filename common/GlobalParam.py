# coding=utf-8
import os, sys
import ConfigParser
import Log

logger = Log.getLogger();

absurl = os.path.dirname(os.path.dirname(__file__));
fileurl = absurl + os.path.sep + 'file' + os.path.sep ;
filename = fileurl + 'session.txt';
filename = fileurl + 'session.conf';

class GLParams():
    global filename;
    def __init__(self):
        self.conf = ConfigParser.ConfigParser();
        self.section = 'session';
        # self.add_section(self.section)

    def add(self, key, value):
        if self.conf.has_section(self.section)==False:
            self.conf.add_section(self.section);
        
        self.conf.set("session", key, value);
        with open(filename, 'w') as configfile:
            self.conf.write(configfile);
 
       
        
    def get(self, key):
        self.conf.read(filename);
        value = self.conf.get(self.section, key);
        return value;

'''
gl = GLParams();
gl.add('mobile', '123')
gl.add('token', 'fdsafasdfsadf')
gl.add('id', 'dfsafsadfsaf')
gl.add('mobile', '123')

print gl.get('mobile')
'''

'''     
import ConfigParser
# 创建配置文件对象，创建对象的2个写法均可
# config=ConfigParser.RawConfigParser()
config = ConfigParser.ConfigParser()


# add a section(添加一个新的section)
config.add_section('section1')
# 对section1添加配置信息
config.set('section1', 'name', 'xiaodeng')
config.set('section1', 'age', '28')


print config

# 添加第二个section
config.add_section('section2')
# 对section1添加配置信息
config.set('section2', 'name', 'fengmei')
config.set('section2', 'age', '18')
config.set('section1', 'sex', '1')

# 添加第二个section

# 对section1添加配置信息
config.set('section2', 'name1', 'fengmei')
config.set('section2', 'age1', '18')
config.set('section1', 'sex1', '1')


# 用上下文管理器的方式打开配置文件并写入配置信息
with open('test.cfg', 'w') as configfile:
    config.write(configfile)
'''
