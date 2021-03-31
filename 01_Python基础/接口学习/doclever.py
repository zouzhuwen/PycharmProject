import requests

class Doclever():
    def __init__(self):
        self.res_se = requests.session()


    def login(self):
        """登录"""
        url = 'http://www.doclever.cn:8090/user/login'
        params = {'name':'zouzhuwen','password':1234}
        r = self.res_se.post(url=url,data=params)

        # 获取email
        email = r.json().get('data').get('email')
        # 获取id
        userid = r.json().get('data').get('_id')

        return {"email":email,"userid":userid}


    def editage(self):
        """修改年龄"""
        dict = self.login()
        email = dict.get("email")
        userid = dict.get("userid")
        url = 'http://www.doclever.cn:8090/user/save'
        data = {'age':18,'email':email,'userid':userid}

        r = self.res_se.post(url=url,data=data)
        return r.text



    def editpass(self):
        """修改密码"""
        dict = self.login()
        # email = dict.get("email")
        userid = dict.get("userid")
        data = {'userid':userid,'oldpass':1234,'newpass':123}
        url = 'http://www.doclever.cn:8090/user/editpass'

        r = self.res_se.put(url=url,data=data)
        return r.text



if __name__ == '__main__':
    d = Doclever()
    #修改年龄
    print(d.editage())
    #修改密码
    print(d.editpass())
