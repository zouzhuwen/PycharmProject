# xiaoming_dict={"name":"小明",
#           "qq":123456,
#           "phone":"10086"}
#
# # 迭代遍历字典
# # 变量k是每次循环中，获取到的键值对的key
#
# for k in xiaoming_dict:
#     print("%s-%s" %(k,xiaoming_dict[k]))

card_list=[
    {"name":"zhangsan",
     "qq":"123456",
     "phone":"110"},
    {"name":"lisi",
     "qq":"54321",
     "phone":"10086"},
    {}
]

for card_info in card_list:
    print(card_info)