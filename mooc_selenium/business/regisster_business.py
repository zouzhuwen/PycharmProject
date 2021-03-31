#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    #信息输入
    def base_info(self,email,name,password,file_path):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_path)
        self.register_h.click_register_button()

    #邮箱错误
    def login_email_error(self,email,name,password,file_path):
        self.base_info(email,name,password,file_path)
        if self.register_h.get_user_text("email_error","请输入有效的电子邮件地址"):
            print("邮箱检验成功")
            return False
        else:
            return True
    #主方法
    def register_function(self,email,name,password,file_path,assertCode,assertText):
        self.base_info(email, name, password, file_path)
        if self.register_h.get_user_text(assertCode, assertText):
            print("邮箱检验成功")
            return False
        else:
            return True



    def login_name_error(self,email,name,password,file_path):
        self.base_info(email,name,password,file_path)
        if self.register_h.get_user_text("name_error", "字符长度必须大于等于4，一个中文字算2个字符"):
            print("名称检验成功")
            return False
        else:
            return True

    def login_password_error(self, email, name, password, file_path):
        self.base_info(email, name, password, file_path)
        if self.register_h.get_user_text("password_error", "最少需要输入 5 个字符"):
            print("密码检验成功")
            return False
        else:
            return True

    def login_code_error(self, email, name, password, file_path):
        self.base_info(email, name, password, file_path)
        if self.register_h.get_user_text("password_error", "验证码错误"):
            print("验证码检验成功")
            return False
        else:
            return True

    def login_succeed(self, email, name, password, file_path):
        self.base_info(email, name, password, file_path)
        if self.register_h.get_register_button():
            print("点击注册后能找到，注册按钮")
            return False
        else:
            return True


        self.register_h.send_user_name()
        self.register_h.send_user_password()
        self.register_h.send_user_code()