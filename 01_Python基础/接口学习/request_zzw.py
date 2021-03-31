import requests


def request():
    ak = 'CuSKN7YgYtL1aG4EmOLAjKvUeGxrA7ol'
    url_params = {'query':'银行','bounds':'39.915,116.404,39.975,116.414',
                  'output':'json','ak':ak}

    url = 'http://api.map.baidu.com/place/v2/search'
    res = requests.get(url,params=url_params)
    res.encoding = 'utf-8'  # 设置编码

    # 以json格式，显示响应
    result = res.json()
    #第一个请求
    print(url)
    #第一个请求的响应结果
    print(result)

    #获取lat
    lat = str(result['results'][0]['location']['lat'])
    # 获取lng
    lng = str(result['results'][0]['location']['lng'])

    print("==========================")
    #查找停车点
    location = lat+''+','+''+lng
    #print(location) #  校验location
    url_park = ' http://api.map.baidu.com/parking/search'
    url_params_park = {'ak':ak,'location':location,'coordtype':'bd09ll'}
    res_park = requests.get(url_park,params=url_params_park)

    # 以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
    res_park.encoding = 'utf-8'
    #第二个请求
    print(url_park)
    #第二个请求的响应结果
    print(res_park.text)


if __name__ == '__main__':
    request()