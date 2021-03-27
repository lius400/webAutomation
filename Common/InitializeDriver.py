# --^_^-- coding:utf-8 --^_^--
# @Remark:初始化webdriver

# 自定义请求头head
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 设置自定义请求头参数
def get_headers_driver():
    # 负责启动服务端时的参数设置
    desire = DesiredCapabilities.CHROME.copy()
    headers = {'Accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64',
               'Connection': 'keep-alive'
               }
    for key, value in headers.items():
        desire['chrome.page.customHeaders.{}'.format(key)] = value

    # 将yes改成no可以让浏览器不加载图片
    driver = webdriver.Chrome(desired_capabilities=desire, service_args=['--load-images=yes'])
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver
