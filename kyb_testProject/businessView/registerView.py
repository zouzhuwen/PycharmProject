from common.common_fun import Common,NoSuchElementException
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
import random
import logging

class RegisterView(Common):
    register_text=(By.ID,"com.tal.kaoyan:id/login_register_text")#登录页注册icon

    register_userheader = (By.ID, "com.tal.kaoyan:id/activity_register_userheader")#注册页头像icon
    item_image = (By.ID, "com.tal.kaoyan:id/item_image")#选择头像
    save_image = (By.ID, "com.tal.kaoyan:id/save")#保存头像

    #用户名密码邮箱相关元素
    register_username = (By.ID, "com.tal.kaoyan:id/activity_register_username_edittext")#注册用户名
    register_password = (By.ID, "com.tal.kaoyan:id/activity_register_password_edittext")#注册密码
    register_emaill = (By.ID, "com.tal.kaoyan:id/activity_register_email_edittext")#注册邮箱
    register_btn = (By.ID, "com.tal.kaoyan:id/activity_register_register_btn")#注册页注册按钮

    #完善资料界面元素 选择院校
    perfectinfomation_school = (By.ID, "com.tal.kaoyan:id/perfectinfomation_edit_school_name")
    university_city = (By.ID, "com.tal.kaoyan:id/more_forum_title")
    university_name = (By.ID, "com.tal.kaoyan:id/university_search_item_name")

    #完善资料界面元素 专业选择
    perfectinfomation_major = (By.ID, "com.tal.kaoyan:id/activity_perfectinfomation_major")
    subject = (By.ID, "com.tal.kaoyan:id/major_subject_title")
    subject_group = (By.ID, "com.tal.kaoyan:id/major_group_title")
    subject_name = (By.ID, "com.tal.kaoyan:id/major_search_item_name")

    # 点击进入考研帮
    perfectinfomation_goBtn=(By.ID, "com.tal.kaoyan:id/activity_perfectinfomation_goBtn")

    button_mysefl = (By.ID, "com.tal.kaoyan:id/mainactivity_button_mysefl")  # 我tab
    username = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")  # 登录后的用户名

    def register_action(self,register_username,register_password,register_emaill):
        self.check_cancelBtn()#检测升级弹窗
        self.check_skipBtn()#检测跳过按钮

        logging.info("=====register_action======")
        self.driver.find_element(*self.register_text).click()#点击注册按钮

        logging.info("set userhead")
        self.driver.find_element(*self.register_userheader).click()
        self.driver.find_elements(*self.item_image)[2].click()#选择头像
        self.driver.find_element(*self.save_image).click()

        logging.info("username is %s"%register_username)
        self.driver.find_element(*self.register_username).send_keys(register_username)

        logging.info("password is %s" % register_password)
        self.driver.find_element(*self.register_password).send_keys(register_password)

        logging.info("email is %s" % register_emaill)
        self.driver.find_element(*self.register_emaill).send_keys(register_emaill)

        self.find_element(*self.register_btn).click()

        #检测是否登录成功
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            #注册失败
            logging.error("register fail!")
            self.getScreenShot("register fail!")
            return False
        else:
            #注册成功
            self.add_register_info()#完善资料
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info("=====add_register_info======")

        logging.info("select school...")
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.university_city)[1].click()
        self.driver.find_elements(*self.university_name)[1].click()

        logging.info("select major...")
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.subject)[1].click()
        self.driver.find_elements(*self.subject_group)[2].click()
        self.driver.find_elements(*self.subject_name)[1].click()

        self.find_element(*self.perfectinfomation_goBtn).click()


    def check_register_status(self):
        logging.info("====check_register_status====")
        self.check_market_ad()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error("register Fail!")
            self.getScreenShot("register fail!")
            return False
        else:
            logging.info("register success!")
            return True


if __name__ == '__main__':
    driver=appium_desired()
    # 设置随机的用户名、密码、邮箱
    username = "zxw2018" + "zzw" + str(random.randint(1000, 90000))
    password = "zxw2018" + str(random.randint(1000, 90000))
    email = "51zxw" + str(random.randint(1000, 90000)) + "@163.com"
    register=RegisterView(driver)
    register.register_action(username,password,email)











