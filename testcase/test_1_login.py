# coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import login_page
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case

# username = "13800138001"
# password = "yungehuo2019"

@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    def test_01_login(self, data):
        """正常登录"""

        test_data = data['data']
        test_assert = data['assertion']
        login = login_page.Login(self.dr)
        ele = login.login(test_data['username'],test_data['password'])
        # login.login(username,password)  # 不取表格数据直接传参
        login.exist_loading()
        username = login.get_name()
        url = login.get_url()
        self.assertIn(url,test_assert['title'])
        self.assertIn(username, test_assert['username'])

