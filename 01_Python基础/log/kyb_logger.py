import yaml
from appium import webdriver
import logging
from selenium.common.exceptions import NoSuchElementException

#读取desired_caps.yaml配置表信息
file = open("../yaml/desired_caps.yaml","r",encoding="UTF-8")
data = yaml.load(file)

#日志配置
logging.basicConfig(level=logging.INFO,filename="runlog.log",
                    format="%(asctime)s %(filename)s[line:%(lineno)d] [%(levelname)s] %(message)s")

desired_cap = {}
desired_cap["platformName"] = data["platformName"]
desired_cap["platformVersion"]=data["platformVersion"]
desired_cap["deviceName"]=data["deviceName"]
desired_cap["app"]=data["app"]
desired_cap["appPackage"]=data["appPackage"]
desired_cap["noReset"]=data["noReset"]
desired_cap["ip"]=data["ip"]
desired_cap["port"]=data["port"]

driver=webdriver.Remote("http://"+str(data["ip"])+":"+str(data["port"])+"/wd/hub",desired_cap)
logging.info("start app...")
driver.implicitly_wait(5)

def check_cancelBtn():
    logging.info("check_cancelBtn")
    try:
        cancelBtn = driver.find_element_by_id("android:id/button2")
        cancelBtn.click()
    except NoSuchElementException:
        logging.info("no cancelBtn")

def check_skipBtn():
    logging.info("check_skipBtn")
    try:
        skipBtn = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
        skipBtn.click()
    except NoSuchElementException:
        logging.info("no skipBtn")


check_cancelBtn()
check_skipBtn()

