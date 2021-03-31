import requests
import json
from 数据读写.EXCEL.my_excel import read_data,write_data,add_sheet


def query(start,end,page,size):
    url = 'http://221.176.34.113:8761/andfans-activity/report/query'
    headers = {'Content-Type':'application/json;charset=UTF-8'}
    data = {'start':start,'end':end,'page':page,'size':size}
    rs = requests.post(url,data=json.dumps(data),headers=headers)
    # print(rs.text)
    # print(rs.json())
    return rs.json() #  返回json的结果


def result():
    data = read_data(r'C:\Users\hp\Desktop\testcase.xlsx','Sheet')
    # print(data) #  原来的表，二维数组
    for i in range(len(data)):
        if i==0:
            continue
        reponse = query(str(data[i][0]),str(data[i][1]),data[i][2],data[i][3]) # [0][1][2][3]分别为start、end,page,size
        msg = reponse['msg'] #  获取请求返回的msg
        # print(msg)
        # print(data[i])
        data[i].append(msg) # 把msg添加到data中的每一列
        if str(msg)==data[i][5]: #  判断msg和预期结果是否为一致 一致pass 否则 fail
            data[i].append("pass")
        else:
            data[i].append("fail")

    add_sheet(r'C:\Users\hp\Desktop\testcase.xlsx',data,'result') #增加一个result表格





if __name__ == '__main__':
    # query(1,1,1,1)
    result()
