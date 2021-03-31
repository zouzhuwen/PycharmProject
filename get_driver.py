# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/5/005
from appium import webdriver
import os

class driver_configure():
    def __init__(self):
        de=os.popen("adb shell getprop ro.boot.serialno")
        ve = os.popen ("adb shell getprop ro.build.version.release")
        self.devicenName= de.read().replace('\n', '')
        self.getVersion=ve.read().replace('\n', '')
    def get_driver(self):
        '''获取driver'''
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            self.desired_caps['deviceName'] = self.devicenName  # 手机ID
            self.desired_caps['platformVersion'] = self.getVersion  # 系统版本
            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['appPackage'] = 'com.cmic.college'     # APK包名
            self.desired_caps['appActivity'] = 'com.cmcc.cmrcs.android.ui.activities.WelcomeActivity'     # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = 'true' # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '120' # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
            #self.desired_caps['automationName'] = "uiautomator2"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
            return self.driver
        except Exception as e:
            raise e
if __name__ == '__main__':
    dr=driver_configure()
    dr.get_driver()