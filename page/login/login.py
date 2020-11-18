"""
mailiangche_UI - 当前Project名称;
login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/13 5:21 下午 
"""
from time import sleep

from page.base.basepage import BasePage


class Login(BasePage):

    def goto_login(self):
        self.po_run('goto_login')
        return Login(self.driver)

    def login(self,cellphone,code):
        self.po_run('login',cellphone=cellphone,code=code)
        return Login(self.driver)

    def logout(self):
        self.po_run('logout')
        return Login(self.driver)

    def close_alert(self):
        sleep(10)
        self.po_run('close_alert')
        return Login(self.driver)

class InfoAdd(BasePage):
    pass