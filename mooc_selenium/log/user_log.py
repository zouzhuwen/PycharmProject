#coding=utf-8
import  logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)

        #logger.setLevel(logging.WARN)
        #控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug("1111111111")

        #文件名称
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file

        #文件日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s %(filename)s-->%(funcName)s %(levelno)s: %(levelname)s--->%(message)s")
        # self.file_handle.setLevel(logging.INFO)
        # self.file_handle.setLevel(logging.DEBUG)
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        #logger.debug("test1234")
        #logger.WARNING("error")
        # consle.close()
        # logger.removeHandler(consle)



    def get_log(self):
        return  self.logger


    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug("1111")
    user.close_handle()