webAutomation

WebDriver自动化测试框架，使用POM模式；

分为四层：对象库层、逻辑层、业务层、数据层；

项目层级：

1.Common：主要放封装好的定位元素方法、项目的路径配置、测试报告的方法库、自定义的logging模块等

2.Outputs：主要放log日志、测试报告、测试截图等

3.PageLocators：主要放web页面的定位元素

4.PageObjects：主要放各页面的业务功能

5.TestCases：主要放测试用例根据Python+unittest或者Python+pytest进行测试用例的封装

6.TestDatas：主要放测试数据

7.main.py：最后在项目下有一个main.py文件，就是项目的入口。