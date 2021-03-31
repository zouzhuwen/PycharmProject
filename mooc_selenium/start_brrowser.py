#coding=utf-8
from selenium import webdriver
import  time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from read_image import read

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
#http://www.5itest.cn/register
driver.maximize_window()
time.sleep(5)

print(expected_conditions.title_contains("注册"))#检测标题是否存在
locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(expected_conditions.visibility_of_element_located(locator))#检测元素是否显示


#获取元素中的值 邮箱
user_email = ''.join(random.sample("abcdefgh0123456789",5))+"@163.com"
email_element = driver.find_element_by_name("email")
email_element.send_keys(user_email)
print(email_element.get_attribute("value"))
#用户名
element_node = driver.find_elements_by_class_name("controls")[1]
element_node.find_element_by_class_name("form-control").send_keys("zz0w123456")
#密码
driver.find_element_by_id("register_password").send_keys("12345")
def auth_code():
    driver.save_screenshot("E:/imooc.png")
    code_element = driver.find_element_by_id("getcode_num")
    x = code_element.location["x"]#左下角X坐标
    y = code_element.location["y"]#左下角Y坐标
    width = code_element.size["width"]+x#右上角X坐标
    height = code_element.size["height"]+y#右上角Y坐标
    im = Image.open("E:/imooc.png")
    img = im.crop((x,y,width,height))
    img.save("E:/imooc1.png")

    text= read("E:/imooc1.png");
    return text

#验证码
code = auth_code()
print(code)
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(code)

time.sleep(8)
driver.close()