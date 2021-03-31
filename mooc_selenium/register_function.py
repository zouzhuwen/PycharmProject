#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
import pytesseract
from find_element import FindElement

class Register_function(object):
    def __init__(self,url,i):
        self.driver =self.get_driver(url,i)

        #获取driver并打开url
    def get_driver(self,url,i):
        if i==1:
            driver = webdriver.Chrome()
        elif i==2:
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Edge()

        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        return  driver

        # 获取element信息
    def find_element(self,key):
        element =FindElement(self.driver).get_elemet(key)
        return element

        #输入用户信息
    def send_user_info(self,key,data):
        element =self.find_element(key)
        element.send_keys(data)


        # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample("0123456789abcdefghijk", 8))
        return user_info

        # 获取图片
    def get_code_image(self,file_path):
        self.driver.save_screenshot(file_path)
        code_element = self.driver.find_element_by_id("getcode_num")
        x = code_element.location["x"]  # 左下角X坐标
        y = code_element.location["y"]  # 左下角Y坐标
        width = code_element.size["width"] + x  # 右上角X坐标
        height = code_element.size["height"] + y  # 右上角Y坐标
        im = Image.open(file_path)
        img = im.crop((x, y, width, height))
        img.save(file_path)

        # 拆解图片获取验证码
    def code_online(self,file_path):
        self.get_code_image(file_path)
        image = Image.open(file_path)
        # 置灰处理
        image = image.convert("L")
        # 这个是二值化阈值
        threshold = 156
        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了
        image = image.point(table, "1")
        # image.show()
        text = pytesseract.image_to_string(image)
        return text

    def main(self):
        # 运行主程序
        user_info = register.get_range_user()
        email = user_info + "@163.com"
        image_path = "E:/imooc2.png"
        self.send_user_info("user_email",email)
        self.send_user_info("user_name", user_info)
        self.send_user_info("password", "111111")
        self.get_code_image(image_path)
        text = self.code_online(image_path)
        print(text)
        self.send_user_info("code_text",text)
        self.find_element("register-btn").click()

        if self.find_element("captcha_code-error") == None:
            print("注册成功...")
        else:
            print("注册失败...")
            self.driver.save_screenshot("E:/captcha_code-error.png")

        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    for i in  range(3):
        register = Register_function("http://www.5itest.cn/register",i)
        register.main()