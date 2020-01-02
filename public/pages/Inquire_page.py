# coding=utf-8
import time
from public.common import basepage

class Inquire(basepage.Page):
    """运价查询页面"""

    def click_shipment_address(self):
        """点击发货地址输入框"""
        self.dr.click('css->form.searchbox.design-width>span:nth-child(1)')
        time.sleep(1.5)

    def click_delivery_address(self):
        """点击收货地址输入框"""
        self.dr.click('css->form.searchbox.design-width>span:nth-child(2)')
        time.sleep(1.5)

    def click_adress(self, num, city):
        """再次封装省/市/区/街道"""
        self.dr.click_province('css->div.ivu-poptip-popper.v-picker.picker-index.v-transfer-dom',
                      '//div/div[2]/div/div/section/div[2]/div[{}]//descendant::a'.format(num), city)
        time.sleep(1.5)

    def report_btn(self):
        """点击一键报价按钮"""
        self.dr.click('class->button.button.m-btn.primary')
        time.sleep(5)
