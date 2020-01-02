# coding=utf-8
import time
import unittest
from public.common import mytest
from public.pages import Inquire_page
from loguru import logger
from public.pages import login_page
from ddt import ddt,data,unpack
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestInquire(mytest.MyTest):
    """运价查询模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    def test_01_inquire(self,data):
        """一键报价流程"""

        logger.info(data)
        test_data = data['data']
        login = login_page.Login(self.dr)
        ele = login.login(test_data['username'], test_data['password'])
        inquire = Inquire_page.Inquire(self.dr)
        inquire.click_shipment_address()
        inquire.click_adress(1, '广东省')
        inquire.click_adress(2, '清远市')
        inquire.click_adress(3, '连南瑶族自治县')
        inquire.click_adress(4, '大麦山镇')
        inquire.click_delivery_address()
        inquire.click_adress(1, '福建省')
        inquire.click_adress(2, '莆田市')
        inquire.click_adress(3, '城厢区')
        inquire.click_adress(4, '凤凰山街道')
        inquire.report_btn()


