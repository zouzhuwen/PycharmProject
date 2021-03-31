#coding=utf-8
from PIL import Image
import pytesseract

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver

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
