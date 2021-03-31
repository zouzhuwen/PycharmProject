# -*- coding: utf-8 -*-
import logging
from common.common_fun import Common,NoSuchElementException
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired

class LoginView(Common):
    username_type=(By.ID,"com.tal.kaoyan:id/login_email_edittext")#登录账号
    password_type=(By.ID,"com.tal.kaoyan:id/login_password_edittext")#登录密码
    loginBtn=(By.ID,"com.tal.kaoyan:id/login_login_btn")#登录按钮

    tip_commit=(By.ID,"com.tal.kaoyan:id/tip_commit")
    button_mysefl=(By.ID,"com.tal.kaoyan:id/mainactivity_button_mysefl")#我tab
    username = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")  #登录后的用户名

    RightButton=(By.ID,"com.tal.kaoyan:id/myapptitle_RightButton_textview")#我模块设置按钮
    logout = (By.ID, "com.tal.kaoyan:id/setting_logout_text")#个人设置 退出登录按钮



    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("=========login_action========")
        logging.info("username is %s"%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info("password is %s"%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn).click()
        #logging.info("login finished!")

    def check_account_alert(self):
        logging.info("=======check_account_alert========")
        try:
            element=self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info("close tip_commit")
            element.click()

    def check_loginStatus(self):
        logging.info("=====check_loginStatus=====")
        self.check_market_ad()
        self.check_account_alert()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)

        except NoSuchElementException:
            logging.error("login Fail!")
            self.getScreenShot("login fail!")
            return False
        else:
            logging.info("login success!")
            self.logout_action()
            return True

    def logout_action(self):
        #退出登录
        logging.info("====logout_action====")
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logout).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
     driver=appium_desired()
     l=LoginView(driver)
     l.login_action("自学网2018","zxw2018")
     l.check_loginStatus()


