#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 10:48
# @Author  : yxChen

class Node:
    def __init__(self,method,positon,xpath,text,nodeBound,nodeBoundPosition):
        self.method=method
        self.nodeBoundPosition=nodeBoundPosition
        self.positon=positon
        self.xpath=xpath
        self.text=text
        self.nodeBound=nodeBound
    def __str__(self):
        mes='[method: %s,position: %s, xpath: %s,text: %s,nodeBound: %s,nodeBoundPosition: %s]'\
            %(self.method,str(self.positon),self.xpath,self.text,str(self.nodeBound),str(self.nodeBoundPosition))
        return mes
    def getStr(self):
        return self.__str__()


