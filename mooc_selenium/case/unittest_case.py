#coding=utf-8
import unittest

class FirstCase01(unittest.TestCase):

    #装饰器
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("这是前置条件")
    @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("这是第一条case")

    def testfirst02(self):
        print("这是第二条case")

    def testfirst03(self):
        print("这是第三条case")

    def tearDown(self):
        print("这是后置条件")





if __name__ == '__main__':
    # unittest.main()

    #容器
    sutie=unittest.TestSuite()
    sutie.addTest(FirstCase01('testfirst03'))
    sutie.addTest(FirstCase01('testfirst02'))
    sutie.addTest(FirstCase01('testfirst01'))
    unittest.TextTestRunner().run(sutie)