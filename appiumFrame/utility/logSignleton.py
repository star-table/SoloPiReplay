#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:31
# @Author  : yxChen

import threading,configparser,logging,os

class LogSignleton:
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        '''
        实现单例
        :param args:
        :param kwargs:
        :return:
        '''
        lock=threading.Lock()
        lock.acquire()
        if hasattr(cls,'instance'):
            pass
        else:
            cls.instance=super().__new__(cls)
            conf=configparser.ConfigParser()
            conf.read(os.path.abspath("..")+"/config/logConf.ini",encoding='utf-8')
            cls.instance.logFilePath=os.path.abspath("..")+"/log/"+conf.get('LOGGING', 'log_file')
            cls.instance.logName = conf.get('LOGGING', 'logger_name')
            cls.instance.fmt = conf.get('LOGGING', 'fmt')
            cls.instance.consoleLevel = conf.get('LOGGING', 'log_level_in_console')
            cls.instance.fileLevel = conf.get('LOGGING', 'log_level_in_logfile')
            cls.instance.logger=logging.getLogger(cls.instance.logName)
            #设置logger收集器的根等级
            cls.instance.logger.setLevel(10)
            cls.instance.__configLogger()
        lock.release()
        return cls.instance

    def __configLogger(self):
        '''
        私有方法,配置logger
        :return:
        '''
        fmt=logging.Formatter(self.fmt)
        #控制台输出
        consoloHandle=logging.StreamHandler()
        consoloHandle.setFormatter(fmt)
        consoloHandle.setLevel(int(self.consoleLevel))
        #文件输出
        fileHandle=logging.FileHandler(self.logFilePath,encoding='utf-8',mode='a')
        fileHandle.setFormatter(fmt)
        fileHandle.setLevel(int(self.fileLevel))
        self.logger.addHandler(consoloHandle)
        self.logger.addHandler(fileHandle)

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    t=LogSignleton()
    loggert=t.getLogger()
    loggert.info("info")
    loggert.debug("debug")
    loggert.error("error")