info_tuple=("zhangsan",18,1.75,'zhangsan')

# 1.取值和取索引
print(info_tuple[0])
# 已经知道该数据的内容，根据内容取索引
print(info_tuple.index(18))


# 2.统计计数
print(info_tuple.count("zhangsan"))

# 组中包含的元素个数
print(len(info_tuple))

for my_info in info_tuple:
    print(my_info)