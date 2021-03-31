#coding=utf-8
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeyWordCase():
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil("D:\PycharmProject\mooc_selenium\config\keyword.xls")
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_data(i,3)
                print(is_run)
                if is_run == 'yes': #是否执行
                    method = handle_excel.get_col_data(i,4)
                    send_value = handle_excel.get_col_data(i, 5)
                    handle_value = handle_excel.get_col_data(i, 6)
                    # ''而不是为None
                    # if send_value
                    self.run_method(method, send_value, handle_value)
                    except_result_method = handle_excel.get_col_data(i,7)
                    except_result = handle_excel.get_col_data(i,8)
                    if except_result != '':
                        print("********"+except_result)
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] =="text":
                            result = self.run_method(except_result_method)
                            print("###########" + result)
                            if except_value[1] in result:

                                handle_excel.writer_value(i,9,'pass')
                            else:
                                handle_excel.writer_value(i,9,'fail')
                        elif except_value[0] == "element":
                            result = self.run_method(except_result_method,except_value[1])
                            print(result)
                            if result:
                                handle_excel.writer_value(i,9,'pass')
                            else:
                                handle_excel.writer_value(i,9,'fail')
                        else:
                            print("没有else")
                    else:
                        print("没有预期结果值")








        #拿到行数
        #循环执行每一行
        #if 是否需要执行
            #拿到执行方法
            #拿到操作值
            #if 是否有输入数据
    def get_except_result_value(self,data):
        return  data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        # print(method)
        # print(send_value+"---------->"+handle_value)
        if send_value == "" and handle_value != "":
            result = method_value(handle_value)
        elif send_value == "" and handle_value == "":
            result = method_value()
        elif send_value != "" and handle_value == "":
            result = method_value(send_value)
        else:
            result = method_value(handle_value,send_value)
        return result




if __name__ == '__main__':
    KeyWordCase().run_main()


