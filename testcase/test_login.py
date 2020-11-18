"""
mailiangche_UI - 当前Project名称;
test_login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/13 5:29 下午 
"""
from time import sleep

import pytest

from testcase.test_base import TestBase


class TestLogin(TestBase):

    @pytest.mark.parametrize("cellphone,code,name",[("13777866085","1234","金敏")])
    def test_login(self,cellphone,code,name):
        try:
            # 如果有隐私政策弹框 点击确定
            title_ele = self.app.privacy_title()
            if (title_ele.text == '用户协议和隐私政策'):
                self.app.privacy_agree()
            sleep(1)
        except:
            print('没有用户协议和隐私政策弹框')

        ele = self.app.goto_user()
        print(ele.text)

        print('ele text:' + ele.text)
        if (ele.text == '点击头像登录'):
            self.app.goto_login().login(cellphone,code).close_alert()
        elif (ele.text == name):
            print('已登录')
        else:
            print('登录账号不是需要的账号，退出重新登录')
            self.app.goto_setting().logout().login(cellphone,code).close_alert()

    def test_logout(self):
        ele = self.app.goto_user()
        print(ele.text)

        print('ele text:' + ele.text)
        if (ele.text == '点击头像登录'):
            print('未登录')
        else:
            print('退出登录')
            self.app.goto_setting().logout()