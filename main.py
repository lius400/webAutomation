#!/use/bin/env python3
# --^_^-- coding:utf-8 --^_^--
# @Remark:运行入口

"""
记录一下用例执行过程 - 日志
如果用例失败 - Trackback报错信息 - 失败了截图。
记录一下， 用例的运行时间 - 起始 - 等待的时候，等待时长。
用例、页面对象当中。 用例 = 页面对象 + 测试数据
断言失败了！！ 页面对象方法执行的时候，报错了！！
页面对象-任意功能 = 等待元素可见，等待元素存在、点击、输入、文本获取、属性获取
alert切换、iframe切换、下拉列表、上传。。。
提供测试报告
"""
import unittest
from Common.BeautifulReport import BeautifulReport
from Common.dir_config import *
from Common import logger

# 一、TestLoader装载测试用例
# testloader的用法
# 1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
# 3、使用s

# TestLoader实例化
test_suite = unittest.TestSuite()    # 套件实例化
loader = unittest.TestLoader()   # 收集器实例化

# 将收集到的用例，放到测试套件当中。
test_suite.addTests(loader.discover(testcases_dir))

# 二、BeautifulReport执行测试用例并生成测试结果
result = BeautifulReport(test_suite)

#三、输出测试结果
result.report(filename='web自动化测试报告', description='测试deafult报告', log_path=htmlreport_dir)

# # 二、将测试报告记录到HTML文件
# # 打开一个HTML文件
# fs = open(htmlreport_dir + '/web平台测试报告.html','wb')
#
# # 三、实例化HTML结果到用例运行器
# runner = HTMLTestRunner(fs,title="web测试报告",description="登录页面功能测试！！",tester="伟")
#
# # 四、运行测试套件
# runner.run(test_suite)