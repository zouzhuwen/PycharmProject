import unittest
from common.desired_caps import appium_desired
import logging

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("========setUp===========")
        self.driver=appium_desired()

    def tearDown(self):
        logging.info("=========tearDown=========")
        self.driver.close_app();



