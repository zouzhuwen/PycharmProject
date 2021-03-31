#coding=utf-8
import ddt
from business.regisster_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
import unittest
import time
import sys
from util.excel_util import ExcelUtil
exc = ExcelUtil()
data  = exc.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)
        self.img_path = "D:\PycharmProject\mooc_selenium\image\code.png"

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

    #邮箱、用户名、密码、验证码、错误信息等位元素、错误提示信息
    '''@ddt.data(
        ['132654','mumu','123456',"D:\PycharmProject\mooc_selenium\image\code.png",'email_error','请输入有效的电子邮件地址'],
        ['132654@', 'mumu', '123456', "D:\PycharmProject\mooc_selenium\image\code.png", 'email_error', '请输入有效的电子邮件地址'],
        ['132654@qq.com', 'mumu', '123456', "D:\PycharmProject\mooc_selenium\image\code.png", 'email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack'''
    @ddt.data(*data)
    def test_register(self,data):
        email, name, password, file_path, assertCode, assertText = data
        email_error = self.login.register_function(email,name,password,file_path,assertCode,assertText)
        self.assertFalse(email_error,"注册成功，此条case执行失败")


if __name__ == '__main__':
    file_path = os.path.join(os.path.abspath('..') + '/report/' + 'first_case1.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)

    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description=u"这是第一个测试报告",
                                           verbosity=2)
    runner.run(suite)