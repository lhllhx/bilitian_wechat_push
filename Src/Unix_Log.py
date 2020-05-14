# BiliBiliHelper Python Version
# Copy right (c) 2019 TheWanderingCoel
# 本文件实现了项目的Unix下日志功能,彩色输出以及写入文件
# 无奈ctypes的那个方法无法在Windows以外系统实现
# 只能写了一个在Unix下实现的日志的模块

import os
import sys
import time
from config import config

class Loggger():

    def __init__(self,filename):
        self.filename = filename
        self.level = {
        "debug":0,
        "info":1,
        "warning":2,
        "error":3,
        "critical":4
        }
        self.current_level = self.level[config["Log"]["LOG_LEVEL"]]

    def debug(self,data,level=0):
        if self.current_level > level:
            return
        data = f"{self.timestamp()} - {__file__}[Line:{sys._getframe().f_lineno}] - DEBUG: {data}"
        print("\033[34;1m"+data+"\033[0m")
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(data+"\n")

    def info(self,data,level=1):
        if self.current_level > level:
            return
        data = f"{self.timestamp()} - {__file__}[Line:{sys._getframe().f_lineno}] - INFO: {data}"
        print("\033[32;1m"+data+"\033[0m")
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(data+"\n")

    def warning(self,data,level=2):
        if self.current_level > level:
            return
        data = f"{self.timestamp()} - {__file__}[Line:{sys._getframe().f_lineno}] - WARNING: {data}"
        print("\033[33;1m"+data+"\033[0m")
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(data+"\n")

    def error(self,data,level=3):
        if self.current_level > level:
            return
        data = f"{self.timestamp()} - {__file__}[Line:{sys._getframe().f_lineno}] - ERROR: {data}"
        print("\033[31;1m"+data+"\033[0m")
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(data+"\n")

    def critical(self,data,level=4):
        if self.current_level > level:
            return
        data = f"{self.timestamp()} - {__file__}[Line:{sys._getframe().f_lineno}] - CRITICAL: {data}"
        print("\033[35;1m"+data+"\033[0m")
        with open(self.filename,"a",encoding="utf-8") as f:
            f.write(data+"\n")
    
    def timestamp(self):
        str_time = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
        return str_time

Log = Loggger(os.getcwd()+"/Log1/BiliBiliHelper-"+time.strftime("%Y%m%d", time.localtime())+".log")
