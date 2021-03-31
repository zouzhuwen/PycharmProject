#coding=utf-8
import unittest

class FirstCase02(unittest.TestCase):

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
    def testfirst001(self):
        print("这是第0一条case")

    def testfirst002(self):
        print("这是第0二条case")

    def testfirst003(self):
        print("这是第0三条case")

    def tearDown(self):
        print("这是后置条件")





if __name__ == '__main__':
    unittest.main()

    #容器
    # sutie=unittest.TestSuite()
    # sutie.addTest(FirstCase02('testfirst003'))
    # sutie.addTest(FirstCase02('testfirst002'))
    # sutie.addTest(FirstCase02('testfirst001'))
    # unittest.TextTestRunner().run(sutie)