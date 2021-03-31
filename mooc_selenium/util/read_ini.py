#coding=utf-8
import configparser

class ReadIni():

    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:\PycharmProject\mooc_selenium\config\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)


    def load_ini(self,file_name):

        cf =configparser.ConfigParser()
        cf.read(file_name)
        #r"D:\PycharmProject\selenium\config\LocalElement.ini"
        return cf
        #print(cf.get("RegisterElement","user_name"))

    def get_value(self,key):

        return self.cf.get(self.node,key)

if __name__ =='__main__':
    load = ReadIni()
    value = load.get_value("user_name")
    print(value)