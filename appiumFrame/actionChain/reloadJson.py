#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 11:10
# @Author  : yxChen

import json,sys
from appiumFrame.actionChain.actionInfo import ActionInfo
from appiumFrame.actionChain.node import Node
from appiumFrame.utility.javaUtil import JavaUtil
from appiumFrame.utility.logSignleton import LogSignleton
class ReloadJson:
    def __init__(self):
        self.actionInfo=ActionInfo()
        self.java=JavaUtil()
        self.logger=LogSignleton().getLogger()
        # time.sleep(3)
    def getJson(self,path):
        '''
        将json转换为字典
        :param path:
        :return:
        '''
        with open(path, 'r', encoding='UTF-8') as f:
            loadDict = json.load(f)
            return loadDict

    def reload(self,path):
        '''
        加载json主方法
        :param json:
        :return:
        '''
        jsonValue=self.getJson(path)
        self.actionInfo.setTargetAppPackage(jsonValue['targetAppPackage'])
        operationLog=json.loads(jsonValue['operationLog'])
        steps=operationLog['steps']
        for stepInfo in steps:
            method=stepInfo['operationMethod']['actionEnum']
            try:
                xpath = stepInfo['operationNode']['xpath']
                if xpath != '':
                    xpath="/"+xpath
            except Exception:
                xpath=''
            try:
                position=self.getPosition(stepInfo)
            except Exception:
                position=''
            try:
                text=self.getText(stepInfo)
            except KeyError as e:
                text=''
            except RuntimeError as e:
                self.logger.error(e)
                sys.exit()
            try:
                nodeBound = self.getNodeBound(stepInfo)
            except:
                nodeBound = ''
            try:
                nodeBoundPosition=self.getNodeBoundPosition(stepInfo)
            except KeyError as e:
                nodeBoundPosition = ''
            except RuntimeError as e:
                self.logger.error(e)
                sys.exit()
            node = Node(method, position, xpath, text, nodeBound,nodeBoundPosition)

            self.actionInfo.setNodeList(node)

        return self.actionInfo

    def getNodeBound(self,stepInfo):
        '''
        获取边界百分比
        :param stepInfo:
        :return:
        '''
        screenSizeStr = stepInfo['operationNode']['extra']['screenSize']
        screenSizeList = screenSizeStr.split(',')
        top = stepInfo['operationNode']['nodeBound']['top']
        bottom = stepInfo['operationNode']['nodeBound']['bottom']
        left = stepInfo['operationNode']['nodeBound']['left']
        right = stepInfo['operationNode']['nodeBound']['right']
        return [float(top) / float(screenSizeList[1]), float(bottom) / float(screenSizeList[1]),
                float(left) / float(screenSizeList[0]), float(right) / float(screenSizeList[0])]

    def getText(self,stepInfo):
        '''
        获取输入操作的文本信息
        :param step_info:
        :return:
        '''
        textInit=stepInfo['operationMethod']['operationParam']['text']
        return self.java.javaDecode(textInit)

    def getNodeBoundPosition(self,stepInfo):
        '''
        获取点击点在控件中的位置百分比
        :param stepInfo:
        :return:
        '''
        relativeLocaltionRatioInit = stepInfo['operationMethod']['operationParam'][
            'localClickPos']  # 返回一个列表[x,y],待定修改apk源码
        relativeLocaltionRatioInitDecode = self.java.javaDecode(relativeLocaltionRatioInit)
        relativeLocaltionRatioList = relativeLocaltionRatioInitDecode.split(',')
        relativeLocaltionRatioList[0]=float(relativeLocaltionRatioList[0])
        relativeLocaltionRatioList[1] = float(relativeLocaltionRatioList[1])
        return relativeLocaltionRatioList

    def getPosition(self,stepInfo):
        '''
        通过step获取位置信息
        :param step:
        :return: node_position对象
        '''
        relativeLocaltionRatioInit=stepInfo['operationMethod']['operationParam']['localClickPos']   #返回一个列表[x,y],待定修改apk源码
        relativeLocaltionRatioInitDecode=self.java.javaDecode(relativeLocaltionRatioInit)
        relativeLocaltionRatioList=relativeLocaltionRatioInitDecode.split(',')
        screenSizeStr = stepInfo['operationNode']['extra']['screenSize']
        screenSizeList=screenSizeStr.split(',')
        top = stepInfo['operationNode']['nodeBound']['top']
        bottom = stepInfo['operationNode']['nodeBound']['bottom']
        left = stepInfo['operationNode']['nodeBound']['left']
        right = stepInfo['operationNode']['nodeBound']['right']
        x = (int(right) - int(left)) * float(relativeLocaltionRatioList[0]) + int(left)
        y = (int(bottom) - int(top)) * float(relativeLocaltionRatioList[1]) + int(top)
        ratioPosition=[x/int(screenSizeList[0]),y/int(screenSizeList[1])]
        return ratioPosition


if __name__ == '__main__':
    t=ReloadJson()
    a=t.reload(r'C:\Users\admin\Desktop\ggg-1565599257334.json')
    print(a)
