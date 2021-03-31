#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

        #获取邮箱元素
    def get_email_element(self):
        return  self.fd.get_elemet("user_email")

        #获取用户名元素
    def get_name_element(self):
        return  self.fd.get_elemet("user_name")

        #获取密码元素
    def get_password_element(self):
        return  self.fd.get_elemet("password")

        #获取验证码元素
    def get_code_element(self):
        return  self.fd.get_elemet("code_text")

        #获取验证码元素
    def get_button_element(self):
        return  self.fd.get_elemet("register_btn")

        #获取邮箱错误元素
    def get_email_error_element(self):
        return self.fd.get_elemet("user_email_error")

        # 获取用户名错误元素
    def get_name_error_element(self):
        return self.fd.get_elemet("user_name_error")

        # 获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_elemet("password_error")

        # 获取验证码错误元素
    def get_code_error_element(self):
        return self.fd.get_elemet("code_text_error")




