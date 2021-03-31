#coding=utf-8
from page.register_page import RegisterPage
from util.get_code import GetCode
import unittest
class RegisterHandle(unittest.TestCase):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,name):
        self.register_p.get_name_element().send_keys(name)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self,file_path):
        text = GetCode(self.driver).code_online(file_path)
        self.register_p.get_code_element().send_keys(text)

    #获取文字信息
    def get_user_text(self,info,user_info):
        try :
            if info == "email_error":
                text =  self.register_p.get_email_error_element().text
            elif info== "name_error":
                text = self.register_p.get_name_error_element().text
            elif info== "password_error":
                text = self.register_p.get_password_error_element().text
            elif info== "code_error":
                text = self.register_p.get_code_error_element().text
            return text
        except Exception:
            print(Exception)
    #点击注册
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取注册按钮
    def get_register_button(self):
        return self.register_p.get_button_element()