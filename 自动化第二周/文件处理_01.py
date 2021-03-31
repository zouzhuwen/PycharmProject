# 1.实现用户注册功能
# 用户输入用户名、密码
# 将用户输入的内容按照固定的格式，比如：egon:123，存入文件
# 可以往一个文件中重复注册新的用户名和密码,
# 附加：
# 1、对输入的用户名进行合法性监测，不能以数字开头，且如果输入的用户名已存在于文件中则要求用户重新输入
# 2、对输入的密码进行合法性监测，密码的长度至少6位，并且不能包含特殊字符*&$
user_list = []

def writer(name,password):
    """写入用户名和密码"""
    file = open("user.txt","r+")
    file.read()
    file.writelines("\n"+name+":"+password)
    file.close()

def name_pass(name):
    """判断用户名是不是以数字开头 不是返回True 是返回Flase"""
    if name[0] in ["0","1","2","3","4","5","6","7","8","9"] :
        return False
    else:
        return True

def password_pass(password):
    """判断密码是否符合规格,符合返回True 错误打印提示信息返回False"""
    if len(password) >= 6:
        for s in password:
            if s in ("*","&","$"):
                print("密码不能包含特殊字符：*&$")
                return False
            else:
                return True
    else:
        print("密码不能少于6位！")
        return False

def read():
    """读取用户表，把读取到的用户信息放到user_list列表中"""
    file = open("user.txt", "r")
    while True:

        user = file.readline()
        if not user:
            break #user为空时 break
        name_list = user.strip().split(":")
        user_list.append(name_list[0])


while True:
    name = input("请输入用户名:")
    password = input("请输入密码:")
    read()
    if name in user_list:#用户名在用户字典中
        print("该用户已存在请重新输入！")
        continue
    #判断用户名
    if name_pass(name):
        if password_pass(password):
            writer(name,password)
            print("恭喜%s，注册成功"%name)
            break
        else:
            continue

    else:
        print("用户名不能以数字开头！")
        continue