import requests
import time,random
import hashlib
import json

class RightCenter():
    def __init__(self):
        self.res = requests.session()
        self.appId = '249f511e5f1643458d12baea295f18d6'
        self.appSecret = 'AWPxcug8EzLRylMMskM2IUC9SKNnp2ZO'
        self.host = 'http://221.176.34.113:8761'
        self.headers = {'Content-Type':'application/json'}
        self.appVersion = '210'
        self.timestamp = time.strftime("%Y%m%d%H%M%S")+str(random.randint(111,999))
        self.token = self.get_token()
        self.sign = self.get_sign()

    def get_token(self):
        """获取token"""
        url = 'http://192.168.203.151:13600/SC/v21/family/auth/token'
        data = {'mobile':'13543418221'}
        rs = requests.get(url=url,params=data)
        return rs.json().get("body").get("data") #  返回token


    def get_sign(self):
        """MD5HEX加密大写
        -请求的参数是” ABrcsmCD”取MD5HEX大写，
        A值为appSecret值取MD5HEX大写，
        B值为AppVersion值取MD5HEX大写,
        C值为Token值取MD5HEX大写,
        D值为Timestamp值取MD5HEX大写。
        """
        A = hashlib.md5(self.appSecret.encode("utf-8")).hexdigest().upper()
        B = hashlib.md5(self.appVersion.encode("utf-8")).hexdigest().upper()
        C = hashlib.md5(self.token.encode("utf-8")).hexdigest().upper()
        D = hashlib.md5(self.timestamp.encode("utf-8")).hexdigest().upper()
        sign = hashlib.md5('{}{}rcsm{}{}'.format(A,B,C,D).encode("utf-8")).hexdigest().upper()
        return sign


    def login(self):
        """登录"""
        login_url = self.host+'/rcsmall-portal/user/check'
        data = {
            "appId":self.appId,
            "token":self.token,
            "appVersion":self.appVersion,
            "timestamp":self.timestamp,
            "sign" : self.sign
        }
        rs = self.res.post(login_url,data=json.dumps(data),headers=self.headers)
        print(login_url)
        print(rs.text)


    def homeContent(self):
        """首页内容接口"""
        url = self.host+'/rcsmall-portal/app/homeContent'
        rs = self.res.get(url)
        print(url)
        print(rs.text)


    def getBenefitsCondition(self):
        """权益超市筛选条件接口"""
        url = self.host+'/rcsmall-portal/app/getBenefitsCondition'
        rs = self.res.post(url)
        print(url)
        print(rs.text)


    def getAllBenefits(self):
        """查看全部权益接口 """
        url = self.host+'/rcsmall-portal/app/getAllBenefits'
        rs = self.res.post(url)
        print(url)
        print(rs.text)
        result = rs.json()
        return   result['data']['allBenefits'][0]['onlineBenefitId'] #  返回onlineBenefitId


    def getOnlineBenefitDetail(self):
        """权益超市权益详情"""
        url = self.host+'/rcsmall-portal/app/getOnlineBenefitDetail'
        onlineBenefitId = self.getAllBenefits()
        print(onlineBenefitId)
        data = {"onlineBenefitId":onlineBenefitId}
        rs = self.res.post(url,data=json.dumps(data),headers=self.headers)
        print(url)
        print(rs.text)


    def queryMyBenefits(self):
        """我的权益查询"""
        url = self.host+'/rcsmall-portal/app/queryMyBenefits'
        rs = self.res.post(url)
        print(url)
        print(rs.text)


    def queryMyBenefitDetail(self):
        """我的权益详情接口"""
        url = self.host+'/rcsmall-portal/app/queryMyBenefitDetail'
        rs = self.res.post(url)
        print(url)
        print(rs.text)


if __name__ == '__main__':
    user = RightCenter()

    user.login()
    user.homeContent()
    user.getAllBenefits()
    user.getBenefitsCondition()
    user.getOnlineBenefitDetail()
    user.queryMyBenefits()
    user.queryMyBenefitDetail()

    

