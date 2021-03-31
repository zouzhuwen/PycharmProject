# coding:utf-8
# 读写csv文件
import csv
import sys
from collections import OrderedDict
import json
import importlib
# importlib.reload(sys)



def read_csv2dicts(csv_file_path, field_names=None):
    '''
    读取csv文件数据到到字典列表中，支持指定特定的列、指定特定的列顺序读取
    :param csv_file_path: csv文件路径
    :param field_names: 指定的列名列表
    '''
    with open(csv_file_path, 'r',encoding='utf-8') as csv_file:
        # 读取csv文件表头列名列表
        header_line = csv_file.readlines()[0]
        headers = header_line.strip().split(',')
        # print(header_line)
        # print(headers)
    # 用二进制格式读取csv文件
    with open(csv_file_path, 'r',encoding='utf-8') as csv_file:
        # 用csv文件对象构建reader对象，reader对象可以看作是多个字典的列表（每行一个字典）
        reader = csv.DictReader(csv_file)
        # for i in reader:
        #     print(i)
        # # 行数据列表（每行数据为一个有序字典）
        datas = []
        for row_dict in reader:
            # 行数据JSON字符串
            row_json_str = ''
            # 使用有序字典，保持指定的列顺序
            # print(row_dict)
            ordered_row_dict = OrderedDict()
            # 根据指定的列名列表过滤
            if field_names:
                # 把原始行数据字典row_dict中的每个字段的数据按照field_names列表的顺序存入ordered_row_dict字典
                for field in field_names:
                    ordered_row_dict[field] = row_dict[field]
                # 因为csv模块只能正常处理ASCII字符，为了正常处理中文，这里还需要做个utf-8编码转换
                # row_json_str = json.dumps(ordered_row_dict).encode('utf-8')
            # 不指定列名的情况，使用csv文件原有表头的列顺序
            else:
                # 指定顺序为原有表头顺序（注：如果不这样处理，csv会自动按照key的字典序进行排序）
                for field in headers:
                    ordered_row_dict[field] = row_dict[field]
                # 因为csv模块只能正常处理ASCII字符，为了正常处理中文，这里还需要做个utf-8编码转换
                # row_json_str = json.dumps(ordered_row_dict).encode('utf-8')
            # 把当前行的数据字典对象添加到datas列表，字典保持原有顺序
            # datas.append(json.loads(ordered_row_dict, object_pairs_hook=OrderedDict))
            datas.append(ordered_row_dict)
        return datas


def write_dicts2csv(dicts, csv_file_path):
    '''
    把数据字典列表写入csv文件
    :param dicts: 数据字典列表
    :param csv_file_path: 要写入的csv文件路径
    '''
    with open(csv_file_path, 'w+',encoding='utf-8') as csv_file:
        # 获取表头列名列表
        headers = dicts[0].keys()
        # lineterminator默认为'\r\n'
        writer = csv.DictWriter(csv_file, fieldnames=headers,lineterminator='\r')
        # 写入表头
        writer.writeheader()
        # 写入数据行
        writer.writerows(dicts)


# 用法示例
def sample():
    # 从csv文件读数据
    datas = read_csv2dicts('./data.csv')
    # print(json.dumps(datas, indent=4))
    # print(datas)

    # 写数据到csv文件
    write_dicts2csv(datas, './new_data.csv')

    print('all finish!')


if __name__ == '__main__':
    sample()
    # field_names = ['name','age','sex']
    # data = read_csv2dicts("data.csv",field_names)
    # for i in data:
    #     print(i)
    #
    # write_dicts2csv(data,'./new_data.csv')
