# --^_^-- coding:utf-8 --^_^--
# @Remark:登录页面元素定位

from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@id="username"]')
    # 密码输入框
    pwd_loc = (By.XPATH, '//input[@id="password"]')
    # 图形验证码
    captche_loc = (By.XPATH,'//img[@id="verifyImg"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//input[@id="formSubmit"]')
    # 密码错误提示信息
    login_error_loc = (By.XPATH, '//button[@class="action-button"]')