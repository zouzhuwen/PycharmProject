#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
from aip import AipOcr

r = ShowapiRequest("http://route.showapi.com/184-5","501719","213c99e1a2c747458d8e19c88e6dc8ec" )
#id:62626  秘钥：d61950be50dc4dbd9969f741b8e730f5  "501719","213c99e1a2c747458d8e19c88e6dc8ec"
r.addBodyPara("img_base64", "E:/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text) # 返回信息

def read(filePath):#pytesseract识别
    image = Image.open(filePath)
    #置灰处理
    image = image.convert("L")
    #这个是二值化阈值
    threshold = 156
    table = []

    for i in  range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    #通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了
    image = image.point(table,"1")
    image.show()
    text = pytesseract.image_to_string(image)
    return text

def read_baidu(filePath):

    """ 你的 APPID AK SK """
    APP_ID = '23491907'
    API_KEY = '1GFxR8XPZVnNpFGVrUpaxIiZ'
    SECRET_KEY = 'syVhyZBf8OcAFTOFtuUnx5Ltfsi86Nsr'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(filePath)

    """ 调用通用文字识别, 图片参数为本地图片 """
    #client.basicGeneral(image);

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "false"
    options["detect_language"] = "false"
    options["probability"] = "false"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    print(client.basicGeneral(image, options))




#print(read("E:/imooc1.png"))
#read_baidu("E:/imooc1.png")