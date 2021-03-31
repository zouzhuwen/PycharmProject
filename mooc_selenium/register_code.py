#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
import pytesseract

driver = webdriver.Chrome()

#浏览器初始化
def init():
    driver.get("http://www.5itest.cn/register")
    time.sleep(5)
    driver.maximize_window()
    print(expected_conditions.title_contains("注册"))  # 检测标题是否存在
    locator = (By.CLASS_NAME, "controls")
    WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(locator))  # 检测元素是否显示

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample("0123456789abcdefghijk",8))
    return user_info

#获取图片
def get_code_image(file_path):
    driver.save_screenshot(file_path)
    code_element = driver.find_element_by_id("getcode_num")
    x = code_element.location["x"]  # 左下角X坐标
    y = code_element.location["y"]  # 左下角Y坐标
    width = code_element.size["width"] + x  # 右上角X坐标
    height = code_element.size["height"] + y  # 右上角Y坐标
    im = Image.open(file_path)
    img = im.crop((x, y, width, height))
    img.save(file_path)

#拆解图片获取验证码
def code_online(file_path):
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
    #image.show()
    text = pytesseract.image_to_string(image)
    return text


#运行主程序
user_info = get_range_user()
emali = user_info+"@163.com"
image_path = "E:/imooc2.png"
init()
get_element("register_email").send_keys(emali)
get_element("register_nickname").send_keys(user_info)
get_element("register_password").send_keys("111111")
get_code_image(image_path)
text = code_online(image_path)
print(text)
get_element("captcha_code").send_keys(text)
get_element("register-btn").click()

time.sleep(3)
driver.close()
