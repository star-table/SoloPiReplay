#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 11:13
# @Author  : yxChen
from appium.webdriver import Remote
from appiumFrame.utility.startUtil import readConfig
from appiumFrame.utility.logSignleton import LogSignleton
import os,re,sys

class DeviceInfo:
    def __init__(self, packagename, udid):
        self.packagename = packagename
        self.activity = self.getActivity(self.packagename)
        self.udid = udid
        self.screenSize=self.getScreenSize()
        self.version=self.getVersion()
        self.logger=LogSignleton().getLogger()

    def getActivity(self,packagename):
        try:
            activity=readConfig(os.path.abspath("..") + "/config/config.ini").get(packagename, 'activity')
        except Exception as e:
            self.logger.error("读取配置文件出错:%s"%e)
            sys.exit()
        return activity

    def getDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = 'Android Emulator'
        # app的信息
        desired_caps['appPackage'] = self.packagename
        desired_caps['appActivity'] = self.activity
        desired_caps['udid']=self.udid
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['autoAcceptAlerts']=True
        try:
            driver=Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
            driver.get_window_size()
        except Exception as e:
            self.logger.error("appium remote driver启动失败,报错信息为: %s"%e)
            sys.exit()
        return driver

    def getVersion(self):
        '''

        :return:获取版本号
        '''
        cmd='adb -s %s shell getprop ro.build.version.release'%self.udid
        version = os.popen(cmd).read().strip()
        return version

    def getScreenSize(self):
        resolution = os.popen('adb -s %s shell wm size' % self.udid).read()
        d = '\d+\.?\d*'
        screenSize = re.findall(d, resolution)
        screenSize=[int(i) for i in screenSize]
        screenSize.sort()
        # print(screenSize)
        return screenSize

if __name__ == '__main__':
    pass
    # readConfig(os.path.abspath("..") + "/config/config.ini").get("a", 'activity')
    # resolution = os.popen('adb -s 127.0.0.1:7555 shell wm size').read()
    # print(resolution)
    # d = '\d+\.?\d*'
    # screenSize = re.findall(d, resolution)
    # screenSize = [int(i) for i in screenSize]
    # screenSize.sort()
    # print(screenSize)
    from appium.webdriver.common.touch_action import TouchAction
    import time
    t=DeviceInfo('com.runx.android','68UDU18208006110')
    driver=t.getDriver()
    driver.implicitly_wait(1)
    time.sleep(8)
    print(1)
    ele = driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ImageView[1]').click()
    print('2')
    TouchAction(driver).long_press(el=ele, duration=2000).release().perform()
    # res=os.system('adb -s 127.0.0.1:7555 shell input tap 248 266')
    # print(res)
