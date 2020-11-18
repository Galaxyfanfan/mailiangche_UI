"""
mailiangche_UI - 当前Project名称;
app.py - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/13 4:45 下午 
"""
from appium import webdriver
from page.base.basepage import BasePage
from page.login.login import Login


class APP(BasePage):
    def privacy_title(self):
        self.po_run('privacy_title')
        return self._current_element

    def privacy_agree(self):
        self.po_run('privacy_agree')
        return APP(self.driver)

    def goto_home(self):
        self.po_run('goto_home')
        return self._current_element

    def goto_user(self):
        self.po_run('goto_user')
        return self._current_element

    def goto_login(self) -> Login:
        self.po_run('goto_login')
        return Login(self.driver)

    def goto_setting(self) -> Login:
        self.po_run('goto_setting')
        return Login(self.driver)


