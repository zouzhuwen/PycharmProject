#coding=utf-8
import xlrd
from xlutils.copy import copy
class ExcelUtil():
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "D:\PycharmProject\mooc_selenium\config\casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

        #[[],[]] 获取excel表格的行数据小list，添加到大list中
    def get_data(self):
        rows = self.get_lines()
        if rows>= 1:
            result = []
            for i in range(self.rows):
                row = self.table.row_values(i)
                result.append(row)
                #print(row)
            return result
        return None

    #获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return  rows
        return None

    #获取单元格数据
    def get_col_data(self,row,col):
        if self.get_lines() >= row:
            data = self.table.cell(row,col).value
            return  data
        return None

    #写入数据
    def writer_value(self,row,col,value):
        read_value = xlrd.open_workbook(self.excel_path)
        writer_data = copy(read_value)
        writer_data.get_sheet(0).write(row,col,value)
        writer_data.save("D:\PycharmProject\mooc_selenium\config\keyword.xls")

if __name__ == '__main__':
    exc = ExcelUtil("D:\PycharmProject\mooc_selenium\config\keyword.xls")
    print(exc.writer_value(7,"test"))