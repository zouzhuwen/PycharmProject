goods = [
{"name": "小米", "price":1999 },
{"name": "VIVO", "price":2999 },
{"name": "华为", "price":3999 },
{"name": "三星", "price":4999 },
{"name": "苹果", "price":5999 },
]
# 启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 用户根据商品编号购买商品
# 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 可随时退出，退出时，打印已购买商品和余额
# 在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

while True:
    msg = [
        ('lenovo', 1200),
        ('dell', 1600),
        ('mac', 1800)
    ]

username="zhangsan"
password ="123"
# while True:
input_username=input("请输入用户名：")
input_password=input("请输入密码：")

if input_username==username and input_password==password :
    salary=input("请输入工资：")
    for list in goods:#遍历列表
        for key in list:
            print(list.get(key))
else:
    print("账号或密码错误！")