#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:39
# @Author  : yxChen
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

from appiumFrame.utility.startUtil import *
from appiumFrame.actionChain.reloadJson import ReloadJson
from appiumFrame.replay.operation import Operation
from appiumFrame.utility.logSignleton import LogSignleton
from appiumFrame.replay.deviceInfo import DeviceInfo
import threading,copy,time

class Start:
    def __init__(self):
        self.logger=LogSignleton().getLogger()

    def main(self):
        filePathList=getFileList()
        udidList=getUdid()
        actionList=[]
        for filePath in filePathList:
            actionInfo = ReloadJson().reload(filePath)
            self.logger.info(actionInfo.get_str())
            actionList.append(actionInfo)
        for udid in udidList:
            threading.Thread(target=self.run,args=(actionList,udid)).start()

    def run(self,actionList,udid):
        for actionInfo in actionList:
            deviceInfo=DeviceInfo(actionInfo.getTargetAppPackage(),udid)
            try:
                driver=deviceInfo.getDriver()

                self.logger.info("设备: %s 启动成功" %udid)
                time.sleep(5)

                # driver.implicitly_wait(3)

            except Exception as e:
                self.logger.error("设备: %s 启动失败,失败信息为: %s" % (udid, e))
                sys.exit()
            operationInstance=Operation(driver,deviceInfo)
            nodeList = copy.deepcopy(actionInfo.getNodeList())
            for node in nodeList:
                try:
                    getattr(operationInstance,node.method)(node)
                except AttributeError as e:
                    self.logger.error("method反射失败,错误信息为: %s"%e)
                    sys.exit()
                finally:
                    time.sleep(2)
            driver.quit()

    # def main(self):
    #     filePathList=getFileList()
    #     udidList=getUdid()
    #     for filePath in filePathList:
    #         actionInfo = ReloadJson().reload(filePath)
    #         self.logger.info(actionInfo.get_str())
    #         for udid in udidList:
    #             threading.Thread(target=self.run,args=(actionInfo,udid)).start()
    #
    # def run(self,actionInfo,udid):
    #     Operation(actionInfo, udid).main()

if __name__ == '__main__':
    # import sys
    # import os
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # print(os.path.split(curPath))
    # rootPath = os.path.split(curPath)[0]
    # print(rootPath)
    # sys.path.append(rootPath)
    Start().main()
    # udid='68UDU18208006110'
    # actionInfo=ReloadJson().reload(os.path.abspath("../")+"/data/啦-1566440335170.json")
    # print(actionInfo)
    # Operation(actionInfo, udid).main()
    # getattr(Start(),'aaa')
    # import os
    # a=os.system("adb -s 127.0.0.1:7555 shell input tap 248 266")
    # print(a)




