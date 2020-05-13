# BiliBiliHelper Python Version
# Copy right (c) 2019 TheWanderingCoel
# 本文件实现了项目的日志功能,彩色输出以及写入文件
# 代码来自于以下两个网站,感谢这些开发者所做的贡献
# https://www.cnblogs.com/nancyzhu/p/8551506.html
# https://www.jianshu.com/p/dcf6bcc1a989

import time
import ctypes
import logging
from config import config
from logging import handlers

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
FOREGROUND_PURPLE = FOREGROUND_RED | FOREGROUND_BLUE

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='[%(asctime)s] - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

    def debug(self,message,color=FOREGROUND_BLUE):
        set_color(color)
        self.logger.debug(message)
        # 不sleep会有info提示变成白色,不知道什么情况
        time.sleep(0.1)
        set_color(FOREGROUND_WHITE)
        
    def info(self,message,color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)
        # 不sleep会有info提示变成白色,不知道什么情况
        time.sleep(0.1)
        set_color(FOREGROUND_WHITE)

    def warning(self,message,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warning(message)
        # 不sleep会有info提示变成白色,不知道什么情况
        time.sleep(0.1)
        set_color(FOREGROUND_WHITE)
    
    def error(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        # 不sleep会有info提示变成白色,不知道什么情况
        time.sleep(0.1)
        set_color(FOREGROUND_WHITE)
    
    def critical(self,message,color=FOREGROUND_PURPLE):
        set_color(color)
        self.logger.critical(message)
        # 不sleep会有info提示变成白色,不知道什么情况
        time.sleep(0.1)
        set_color(FOREGROUND_WHITE)

Log = Logger('./Log/BiliBiliHelper.log',level=config["Log"]["LOG_LEVEL"])