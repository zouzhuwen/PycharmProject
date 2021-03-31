#coding=utf-8
from business.regisster_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
import unittest
import time
from  log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("启动浏览器")
        #self.debug("继续启动——debug")

        self.login = RegisterBusiness(self.driver)
        self.img_path = "D:\PycharmProject\mooc_selenium\image\code.png"
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def tearDown(self):
        time.sleep(2)
        #print(self._outcome.errors)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.abspath("..")+'/report/'+case_name+".png")
                self.driver.save_screenshot(file_path)

        self.driver.close()
        #print("这是后置条件。")

    def test_login_email_error(self):
        email_error = self.login.login_email_error("11","user111","111111",self.img_path)
        self.assertFalse(email_error,"注册成功，此条case执行失败")
        # if email_error :
        #     print("注册成功，此条case执行失败")


    def test_login_username_error(self):
        user_error = self.login.login_name_error("11@163.com","@@@###","111111",self.img_path)
        self.assertFalse(user_error,"注册成功，此条case执行失败")
        # if user_error :
        #     print("注册成功，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("11@163.com", "name11", "11", self.img_path)
        self.assertFalse(password_error,"注册成功，此条case执行失败")
        # if password_error :
        #     print("注册成功，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error("11@163.com", "user12", "111111", self.img_path)
        self.assertFalse(code_error,"注册成功，此条case执行失败")
        # if code_error :
        #     print("注册成功，此条case执行失败")

    def test_login_success(self):
        button = self.login.login_succeed("11@163.com", "user12", "111111", self.img_path)
        self.assertTrue(button,"注册失败，此条case执行失败")
        # if self.login.login_succeed("11@163.com", "user12", "111111", "111111")==False:
        #     print("注册失败，此条case执行失败")


'''
def main():
    fc = FirstCase()
    fc.test_login_email_error()
    fc.test_login_username_error()
    fc.test_login_success()
'''

if __name__ == '__main__':
    unittest.main()
    # file_path = os.path.join(os.path.abspath('..')+'/report/'+'first_case.html')
    # print(file_path)
    # f = open(file_path,'wb')
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    # suite.addTest(FirstCase('test_login_email_error'))
    # # suite.addTest(FirstCase('test_login_username_error'))
    #
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description=u"这是第一个测试报告",verbosity=2)
    # runner.run(suite)