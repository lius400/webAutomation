# --^_^-- coding:utf-8 --^_^--
# @Remark:登录测试数据

from TestDatas.Comm_Datas import web_login_url

# 正常场景
success_data = {"user":"admin","pwd":123456,"check":web_login_url}

# 异常场景1
wrong_datas = [
    {"user":"","pwd":"123456","check":"必填参数为空"},
    {"user":"admin","pwd":"","check":"登录失败，帐号或密码错误"},
    {"user":"adminn","pwd":"123456","check":"账户不存在,请联系管理员"},
    {"user":"admin","pwd":"1234567","check":"登录失败，帐号或密码错误"}
]