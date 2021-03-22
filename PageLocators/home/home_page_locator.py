# --^_^-- coding:utf-8 --^_^--
# @Remark:主页面元素定位

from selenium.webdriver.common.by import By

class HomePageLocator:

    # 主页面LOGO
    logo_loc = (By.XPATH, '//div[@class="logo"]')