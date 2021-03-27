# --^_^-- coding:utf-8 --^_^--
# @Remark:登录页面

from Common.BasePage import BasePage
from PageLocators.login.login_page_locator import LoginPageLocator as loc


class LoginPage(BasePage):
    # 登录功能
    def login(self, username, pwd):
        self.input_text(loc.user_loc, "登录页面_输入用户名", username)
        self.input_text(loc.pwd_loc, "登录页面_输入密码", pwd)
        self.click_element(loc.login_button_loc, "登录页面_点击登录按钮")

    # 获取登录失败提示信息
    def get_errorMsg(self):
        return self.get_element_text(loc.login_error_loc,"登录页面_登录失提示")