#coding=utf-8
import unittest
import os
import sys
sys.path.append("D:\PycharmProject\mooc_selenium")

class RunCase(unittest.TestCase):
    def test_case01(self):
        #case_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        case_path = os.path.join(os.getcwd())
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)





if __name__ == '__main__':
    unittest.main()
    #RunCase().test_case01()