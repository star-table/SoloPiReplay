#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:59
# @Author  : yxChen

from appiumFrame.utility.logSignleton import LogSignleton
from appiumFrame.utility.startUtil import getScreenPath
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys,time,os
class Operation:
    def __init__(self,driver,deviceInfo):
        self.udid=deviceInfo.udid
        self.driver=driver
        self.width=float(deviceInfo.screenSize[0])
        self.height=float(deviceInfo.screenSize[1])
        self.logger=LogSignleton().getLogger()

    def __executeAdb(self,adb):
        adb="adb -s %s shell %s"%(self.udid,adb)
        # print(adb)
        res=os.system(adb)
        if res==0:
            pass
        else:
            self.logger.error("adb命令执行失败.")
            sys.exit()
        return res
    def overrideTap(self,node):
        time.sleep(2)
        # print(node.positon[1])
        # print(self.height)
        self.__executeAdb('input tap %s %s'%(node.positon[0]*self.width,node.positon[1]*self.height))
        time.sleep(2)

    def CLICK(self,node):
        '''点击事件'''
        try:
            self.logger.info("正在执行CLICK事件")
            self.driver.find_element_by_xpath(node.xpath).click()
        except Exception as e:
            self.logger.debug("出错信息{}".format(e))
            try:
                self.overrideTap(node)
            except Exception as e:
                self.logger.error("CLICK事件执行失败,错误信息为: %s" % e)
                screenPath = getScreenPath()
                self.logger.info("错误截图路径为: %s" % screenPath)
                self.driver.save_screenshot(screenPath)
                sys.exit()


    def INPUT(self, node):
        '''输入事件'''
        try:
            self.logger.info("正在执行INPUT事件")
            ele=self.driver.find_element_by_xpath(node.xpath)
            ele.click()
            time.sleep(1)
            ele.send_keys(node.text)
        except Exception as e:
            self.logger.error("INPUT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def INPUT_SEARCH(self,node):
        '''输入并搜索'''
        try:
            self.logger.info("正在执行INPUT_SEARCH事件")
            ele=self.driver.find_element_by_xpath(node.xpath)
            # print(node.text)
            ele.send_keys(node.text)
            time.sleep(1)
            self.driver.press_keycode(keycode=66)
        except Exception as e:
            self.logger.error("INPUT_SEARCH事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SCROLL_TO_RIGHT(self, node):
        '''向右滑动'''
        # self.session.swipe(500, 800, 500, 400, duration=0.4)
        try:
            self.logger.info("正在执行SCROLL_TO_RIGHT事件")
            distance = (node.nodeBound[3] - node.nodeBound[2]) * self.width * float(node.text) * 0.01
            x1 = node.positon[0]*self.width
            y1 = node.positon[1]*self.height
            x2 = x1 + distance
            y2 = y1
            if x2 > (self.width - 10):
                x2 = (self.width - 10)
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("SCROLL_TO_RIGHT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def CLICK_IF_EXISTS(self,node):
        '''发现并点击——待完善'''
        try:
            self.logger.info("正在执行CLICK_IF_EXISTS事件")
            self.driver.find_element_by_xpath(node.xpath).click()
        except Exception as e:
            self.logger.error("SCROLL_TO_RIGHT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SCROLL_TO_LEFT(self, node):
        """从右到左滑动"""
        try:
            self.logger.info("正在执行SCROLL_TO_LEFT事件")
            distance = (node.nodeBound[3] - node.nodeBound[2]) * self.width * float(node.text) * 0.01
            x1 = node.positon[0]*self.width
            y1 = node.positon[1]*self.height
            x2 = x1 - distance
            y2 = y1
            if x2 < 10:
                x2 = 10

            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("SCROLL_TO_LEFT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SCROLL_TO_BOTTOM(self, node):
        """从上到下滑动"""
        # self.session.swipe(500, 400, 500, 800, duration=0.4)
        try:
            self.logger.info("正在执行SCROLL_TO_BOTTOM事件")
            distance = (node.nodeBound[1] - node.nodeBound[0]) * self.height * float(node.text) * 0.01
            x1 = node.positon[0]*self.width
            y1 = node.positon[1]*self.height
            x2 = x1
            y2 = y1 + distance
            if y2 > (self.height - 40):
                y2 = (self.height - 40)
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("SCROLL_TO_BOTTOM事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SCROLL_TO_TOP(self, node):
        """从下到上滑动"""
        # self.session.swipe(500, 800, 500, 400, duration=0.4)
        try:
            self.logger.info("正在执行SCROLL_TO_TOP事件")
            distance = (node.nodeBound[1] - node.nodeBound[0]) * self.height * float(node.text) * 0.01
            x1 = node.positon[0]*self.width
            y1 = node.positon[1]*self.height
            x2 = x1
            y2 = y1 - distance
            if y2 < 40:
                y2 = 40
            # print(x1)
            # print(y1)
            # print(x2)
            # print(y2)
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("SCROLL_TO_TOP事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def GLOBAL_SCROLL_TO_RIGHT(self, node):
        try:
            self.logger.info("正在执行GLOBAL_SCROLL_TO_RIGHT事件")
            distance=self.width//2
            x1=self.width//4
            y1=self.height//2
            x2=x1+distance
            y2=y1
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("GLOBAL_SCROLL_TO_RIGHT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def GLOBAL_SCROLL_TO_LEFT(self, node):
        try:
            self.logger.info("正在执行GLOBAL_SCROLL_TO_LEFT事件")
            distance=self.width//2
            x1=(self.width//4)*3
            y1=self.height//2
            x2=x1-distance
            y2=y1
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("GLOBAL_SCROLL_TO_LEFT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def GLOBAL_SCROLL_TO_BOTTOM(self, node):
        try:
            self.logger.info("正在执行GLOBAL_SCROLL_TO_BOTTOM事件")
            distance=self.height//3
            x1=self.width//2
            y1=self.height//3
            x2=x1
            y2=y1+distance
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("GLOBAL_SCROLL_TO_BOTTOM事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def GLOBAL_SCROLL_TO_TOP(self, node):
        try:
            self.logger.info("正在执行GLOBAL_SCROLL_TO_TOP事件")
            distance=self.height//3
            x1=self.width//2
            y1=(self.height//3)*2
            x2=x1
            y2=y1-distance
            self.driver.swipe(x1, y1, x2, y2)
        except Exception as e:
            self.logger.error("GLOBAL_SCROLL_TO_TOP事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def LONG_CLICK(self, node):
        try:
            self.logger.info("正在执行LONG_CLICK事件")
            # print('0')
            ele = self.driver.find_element_by_xpath(node.xpath)
            # print('1')
            TouchAction(self.driver).long_press(el=ele,duration=int(node.text)).release().perform()
            # print('2')
            # time.sleep(int(node.text)/1000)
        except Exception as e:
            self.logger.debug("出错信息{}".format(e))
            try:
                TouchAction(self.driver).long_press(x=node.positon[0]*self.width,y=node.positon[1]*self.height,duration=int(node.text)).release().perform()
                # time.sleep(int(node.text)/1000)
            except Exception as e:
                self.logger.error("LONG_CLICK事件执行失败,错误信息为: %s" % e)
                screenPath = getScreenPath()
                self.logger.info("错误截图路径为: %s" % screenPath)
                self.driver.save_screenshot(screenPath)
                sys.exit()

    def DEVICE_INFO(self, node):
        try:
            self.logger.info("正在执行DEVICE_INFO事件")
            return self.driver.capabilities
        except Exception as e:
            self.logger.error("DEVICE_INFO事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()
    def KILL_PROCESS(self, node):
        try:
            self.logger.info("正在执行KILL_PROCESS事件")
            self.driver.quit()
        except Exception as e:
            self.logger.error("KILL_PROCESS事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def BACK(self, node):
        try:
            self.logger.info("正在执行BACK事件")
            self.driver.press_keycode(keycode=4)
        except Exception as e:
            self.logger.error("BACK事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def HOME(self, node):
        try:
            self.logger.info("正在执行HOME事件")
            self.driver.press_keycode(keycode=3)
        except Exception as e:
            self.logger.error("HOME事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SCREENSHOT(self, node):
        try:
            self.logger.info("正在执行SCREENSHOT事件")
            screenPath = getScreenPath()
            self.driver.save_screenshot(screenPath)
        except Exception as e:
            self.logger.error("SCREENSHOT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SLEEP_UNTIL(self, node):
        '''等待节点出现'''
        try:
            self.logger.info("正在执行SLEEP_UNTIL事件")
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,node.xpath)))
        except Exception as e:
            self.logger.error("SLEEP_UNTIL事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def HANDLE_ALERT(self, node):
        '''弹窗默认允许'''
        # time.sleep(2)
        try:
            self.logger.info("正在执行HANDLE_ALERT事件")
            xpath_list = ["//*[@text='始终允许']", "//*[@text='允许']", "//*[@text='确定']",
                          "//*[@text='好的']"]
            for xpath in xpath_list:
                try:
                    self.driver.find_element_by_xpath(xpath).click()
                    break
                except Exception as e:
                    self.logger.debug(e)
        except Exception as e:
            self.logger.error("HANDLE_ALERT事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def SLEEP(self, node):
        try:
            self.logger.info("正在执行SLEEP事件")
            time.sleep(node.text)
        except Exception as e:
            self.logger.error("SLEEP事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def EXECUTE_SHELL(self, node):
        try:
            self.logger.info("正在执行EXECUTE_SHELL事件")
            self.driver.execute(node.text)
        except Exception as e:
            self.logger.error("EXECUTE_SHELL事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def CLICK_QUICK(self, node):
        try:
            self.logger.info("正在执行CLICK_QUICK事件")
            for i in range(2):
                self.driver.tap(x=node.positon[0]*self.width, y=node.positon[1]*self.height)
        except Exception as e:
            self.logger.error("CLICK_QUICK事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

    def NOTIFICATION(self, node):
        '''打开通知栏'''
        try:
            self.logger.info("正在执行NOTIFICATION事件")
            self.driver.open_notifications()
        except Exception as e:
            self.logger.error("NOTIFICATION事件执行失败,错误信息为: %s" % e)
            screenPath = getScreenPath()
            self.logger.info("错误截图路径为: %s" % screenPath)
            self.driver.save_screenshot(screenPath)
            sys.exit()

if __name__ == '__main__':
    pass
    # d=u2.connect('127.0.0.1:7555')
    # s=d.session(pkg_name='com.runx.android',attach=False)
    # s.implicitly_wait(5)
    # s.xpath('//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ImageView[1]').click()
    # s.xpath('//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.support.v7.widget.au[1]/android.widget.TextView').click()
    # s.xpath('//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText[1]').set_text('啊啊啊')
    # s.click(253.465,300.5656)
    # s.press('HOME')
    # print(s.device_info)
    # print(s.info)
    #
    # # s.swipe_points()
    # # s.swipe(511.4999907,1352.00000128,511.4999907,696.0000012800001)
    # s.swipe(500,500,500,-500)
    # s.swipe_points([[909,1047],[909,391]])
