# coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from config.basic_config import ConfigInit
from loguru import logger
from public.pages.login_page import Login


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser,globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')


class MyAutologinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser,globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))
        self.workbench = Login(self.dr).login('username','password')

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')
