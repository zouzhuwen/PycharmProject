#字典是一个无需的数据集合，使用
xiaoming={"name":"xiaoming",
          "age":18,
          "sex":"boy"}
# print(xiaoming)
# #取值
# print(xiaoming["name"])
#
# # 修改/增加
# xiaoming["name"]="zhangsan"
# xiaoming["hobaby"]="daqiu"
#
# # 删除
# xiaoming.pop("name")


print(xiaoming )

# 统计键值对数量
print(len(xiaoming))

# 合并字典 注意如果合并自定已经包含存在的键值对，会覆盖原有的尖键值对
temp_dict={"height":1.75,
           "age":20}

xiaoming.update(temp_dict)

# 清空字典
xiaoming.clear()

print(xiaoming)

