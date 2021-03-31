#coding=utf-8

class BassPage():
    def __init__(self,driver):
        self.driver=driver


    #打开网页
    def get_url(self,url):
        self.driver.get(url)

    #获取title
    def get_title(self):
        return  self.driver.title


    #定位元素
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

