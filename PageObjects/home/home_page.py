# --^_^-- coding:utf-8 --^_^--
# @Remark:主页面

from Common.BasePage import BasePage
from PageLocators.home.home_page_locator import HomePageLocator as homeloc


class HomePage(BasePage):

    #确认主页是否加载完成
    def check_login_ele_exists(self):
        visible_Logo = True

        try:
            self.wait_eleVisible(homeloc.logo_loc, "等待显示LOGO")
        except:
            visible_Logo = False
        finally:
            return visible_Logo
