from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv
from  time import sleep


class Common(BaseView):
    cancelBtn=(By.ID,"android:id/button2")
    skipBtn=(By.ID,"com.tal.kaoyan:id/tv_skip")

    wemedia_cacel=(By.ID,"com.tal.kaoyan:id/view_wemdia_cacel")

    def check_cancelBtn(self):
        logging.info("==========check_cancelBtn============")
        # self.driver.implicitly_wait(5)
        # print("sleep 5s...")
        # sleep(5)
        try:
            cancelBtn=self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info("no cancelBtn")
        else:
            cancelBtn.click()
            logging.info("==========click cancelBtn==========")

    def check_skipBtn(self):
        logging.info("==========check_skipBtn==========")
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("==========no skipBtn==========")
        else:
            skipBtn.click()
            logging.info("==========click skipBtn==========")

    def get_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y

    def swipeLeft(self):
        logging.info("swipeLeft")
        l = self.get_size()  # 获取屏幕宽，高
        x1 = l[0] * 0.9
        y1 = l[1] * 0.5
        x2 = l[0] * 0.1
        self.driver.swipe(x1, y1, x2, y1, 1000) #左滑操作

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+\
                   "/screenshots/%s_%s.png" %(module,time)
        logging.info("get %s screenshot" %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        logging.info("=======check_market_ad========")
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info("close market ad")
            element.click()

    def get_csv_data(self,csv_file, line):
        logging.info("======get_csv_data======")
        with open(csv_file, "r", encoding="utf-8-sig") as file:
            data = csv.reader(file)
            for index, row in enumerate(data, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    # driver=appium_desired()
    # com=Common(driver)
    # com.check_cancelBtn()
    # #com.check_skipBtn()
    # com.swipeLeft()
    # com.getScreenShot("startApp")
    # list=["这","是","一个","测试","数据"]
    # for i in  range(len(list)):
    #     print(i,list[i])
    #
    # list1 =[{"daf":24},"是","一个","测试","数据"]
    # for index,item in enumerate(list1):
    #     print(index,item)
    pass


