#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 10:29
# @Author  : yxChen


class ActionInfo:
    def __init__(self):
        self.__targetAppPackage=''    #包名
        self.__nodeList=[]             #每个节点步骤的列表,存储node对象
    def getTargetAppPackage(self):
        return self.__targetAppPackage
    def setTargetAppPackage(self,value):
        self.__targetAppPackage=value

    def getNodeList(self):
        return self.__nodeList

    def setNodeList(self,value):
        self.__nodeList.append(value)
    def __str__(self):
        mes='包名为: %s |节点为: '%(self.getTargetAppPackage())
        for i in self.getNodeList():
            mes+="\n"+i.getStr()
        return mes
    def get_str(self):
        return self.__str__()








