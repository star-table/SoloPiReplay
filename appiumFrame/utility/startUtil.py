#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:43
# @Author  : yxChen
from appiumFrame.utility.logSignleton import LogSignleton
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import os,configparser,sys,time

log=LogSignleton().logger
def getUdid():
    '''
    获取设备的udid
    :return:
    '''
    res = os.popen('adb devices').read()
    result=res.split('\n')
    if result[1]=='':
        log.error('未能找到相应的手机设备,错误信息为: %s'%res)
        sys.exit()
    else:
        udidList = []
        for i in range(1, len(result) - 2):
            udidList.append(result[i].split('\t')[0])
        log.info('设备列表为: ' + str(udidList))
        return udidList

def getFileList():
    '''
    获取json文件
    :return:
    '''
    path = os.path.abspath("..") + "/data/"
    fileList = os.listdir(path)
    filePathList = []
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isfile(filePath) and filePath.endswith('.json'):
            filePathList.append(filePath)
    if filePathList==[]:
        log.error("未检测到需要执行的json文件.")
        sys.exit()
    return filePathList

def readConfig(path):
    conf=configparser.ConfigParser()
    if os.path.isfile(path):
        conf.read(path,encoding='utf-8')
        # log.info("成功读取配置文件")
        return conf
    else:
        log.error("%s 配置文件不存在,程序退出."%path)
        sys.exit()

def getScreenPath():
    screenPath = os.path.abspath("..") + "/screen/" + time.strftime('%Y%m%d-%H%M%S.PNG')
    return screenPath

# def ignorePermission(driver):
#
#
#         xpath_list = ["//*[@text='始终允许']", "//*[@text='允许']",  "//*[@text='确定']",
#                       "//*[@text='好的']"]
#         for xpath in xpath_list:
#             try:
#                 driver.find_element_by_xpath(xpath).click()
#             except:
#                 pass
#                 # print(i)
#             finally:
#                 time.sleep(1)
