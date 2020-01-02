# coding=utf-8
import unittest
import HTMLTestRunner
import time
import os
from loguru import logger
from config import globalparam
from public.common import sendmail
from testcase import test_1_login, test_2_inquire
from public.common.mongo_utils import MongoDatabase
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner


path = os.path.join(os.path.abspath('.'),'report', 'logs','test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.add(path)  # 日志初始化

def run(method, test=None):
    if method == 'all':
        test_dir = './testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.path.join(globalparam.report_path, 'TestResult' + now + '.html')
        with open(reportname, 'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(
                stream = f,
                title = 'UI自动化测试报告',
                description = '输出如下报告'
            )
            runner.run(suite)
        # 等待三秒，发送邮件
        time.sleep(3)
        mail = sendmail.SendMail()
        mail.send()

    if method == 'one':
        suit = unittest.TestSuite()
        suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
        runner = unittest.TextTestRunner()
        runner.run(suit)

if __name__ == '__main__':
    # run('one', test_1_login.TestLogin("test_01_login"))
    run('all')
