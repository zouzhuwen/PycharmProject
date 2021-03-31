from common.myunit import StartEnd
import logging,random,unittest
from businessView.registerView import RegisterView

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info("=====test_user_register=====")
        username = "zxw2018" + "zzw" + str(random.randint(1000, 90000))
        password = "zxw2018" + str(random.randint(1000, 90000))
        email = "51zxw" + str(random.randint(1000, 90000)) + "@163.com"

        r=RegisterView(self.driver)
        self.assertTrue(r.register_action(username,password,email))

if __name__ == '__main__':
    unittest.main
