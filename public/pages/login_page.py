# coding=utf-8
import time
from public.common import basepage
from public.pages.Inquire_page import Inquire


class Login(basepage.Page):
    """登录页面"""

    def click_login_btn(self):
        """点击右上角登录按钮"""
        self.dr.click('class->login')

    def input_account(self, account):
        """输入账号"""
        self.dr.type('css->div.form-item.mobile.m-msgtip.ivu-tooltip>div>input', account)

    def input_pw(self, pw):
        """输入密码"""
        self.dr.type('css->div.form-item.password.m-msgtip.ivu-tooltip>div>input[type=password]', pw)

    def click_login_btn_1(self):
        """点击登录按钮"""
        self.dr.click('class->submit')
        time.sleep(1)

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    # def get_title(self):
    #     """获取登录框上的大标题"""
    #     text = self.dr.get_text("class->title")
    #     return text

    def get_name(self):
        """获取右上角名称"""
        name = self.dr.get_text("class->avatar")
        return name

    def login(self, username, password):
        """封装登录函数"""
        self.click_login_btn()
        self.input_account(username)
        self.input_pw(password)
        self.click_login_btn_1()

        return Inquire(self.dr)





