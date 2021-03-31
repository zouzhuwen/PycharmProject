#coding=utf-8
from features.lib.pages.base_page import BassPage
from selenium.webdriver.common.by import By

class RegisterPage(BassPage):
    def __init__(self,context):
        super().__init__(context.driver)

    def send_email(self,email):
        self.find_element(By.ID,"register_email").send_keys(email)

    def send_username(self,username):
        self.find_element(By.ID,"register_nickname").send_keys(username)


    def send_password(self,password):
        self.find_element(By.ID,"register_password").send_keys(password)

    def send_code(self,code):
        self.find_element(By.ID,"captcha_code").send_keys(code)

    def click_registerbtn(self):
        self.find_element(By.ID,"register-btn").click()

    def register_text(self):
        return self.find_element(By.ID,"captcha_code-error").text