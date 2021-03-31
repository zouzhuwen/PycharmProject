import unittest
from BSTestRunner import BSTestRunner
import logging,time
import sys

#工程目录
path="D:\\PycharmProjects\\kyb_testProject\\"
#将工程目录路径添加到pythonPath
sys.path.append(path)

test_dir="../test_case"
report_dir="../reports"

#加载需要测试的模块
discover=unittest.defaultTestLoader.discover(test_dir,"test_login.py")

now=time.strftime("%Y-%m-%d %H-%M-%S")
report_name=report_dir+"/"+now+"test_report.html"

#打开测试报告
with open(report_name,"wb") as f:
    runner=BSTestRunner(stream=f,title="Kyb Test Report",
                        description="kyb Android app test")
    logging.info("start run test case...")
    #运行test_login.py文件
    runner.run(discover)


