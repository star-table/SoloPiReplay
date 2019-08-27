#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 15:17
# @Author  : yxChen

import jpype,os,threading

class JavaUtil:
    jarPath = os.path.abspath('..') + '/utility/solopi-aes.jar'

    def __new__(cls, *args, **kwargs):
        lock = threading.Lock()
        lock.acquire()
        if hasattr(cls, 'instance'):
            pass
        else:
            cls.instance = super().__new__(cls)
            cls.instance.__javaStart()
        lock.release()
        return cls.instance

    def __javaStart(self):
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s"%(JavaUtil.jarPath), "-Dfile.encoding=UTF-8")

    def javaDecode(self,mes):
        lock = threading.Lock()
        lock.acquire()
        JDClass = jpype.JClass("com.polaris.aes.AESUtils")
        res = (JDClass().decrypt(mes, "com.alipay.hulu"))
        # jpype.shutdownJVM()
        lock.release()
        return res

if __name__ == '__main__':
    a=JavaUtil().javaDecode('0BF1ED67E2091631E9BA056D4A8BBB393506827F26051F79A15F03459CE000E6')
    print(a)