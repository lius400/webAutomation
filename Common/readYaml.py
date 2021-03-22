# --^_^-- coding:utf-8 --^_^--
# @Remark:Yaml文件读取

import yaml,os

# 读取login_datas.yaml文件
login_datas = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +"/TestDatas/login_datas.yaml"
print(login_datas)
with open(login_datas, encoding='utf-8') as file:
    data = yaml.full_load(file)
    # print(data)
    keys = list(data.keys())
    print(keys)
    print(data.get(keys[0])[0].keys())