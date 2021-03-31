#2.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
import os
f_name = 'f_name'
f_new_name = 'f_new_name'

old_str = '2'
new_str = '*'

f = open(f_name, 'r', encoding='utf-8')
f_new = open(f_new_name, 'w', encoding='utf-8')

for line in f:
    if old_str in line:#读取每一行内容  查看old_str是否在当前内容中
        new_line = line.replace(old_str, new_str)#将就字符串替换成新字符串
        f_new.writelines(new_line)
    else:
        new_line = line
        f_new.write(new_line)

f.close()
f_new.close()
#os.replace(f_new_name, f_name)
