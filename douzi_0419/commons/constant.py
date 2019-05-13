# encoding=utf_8
# @Author   ： 豆子
# @Function :  文件路径

import os

# 上2级目录
base_dir = os.path.dirname(os.path.dirname(__file__))

# configs目录
configs_dir = os.path.join(base_dir, 'configs')
# 基础数据路径
basedata_dir = os.path.join(configs_dir, 'basedata.conf')
# 全局数据路径
global_dir = os.path.join(configs_dir, 'global.conf')
# 正式环境数据路径
online_dir = os.path.join(configs_dir, 'online.conf')
# 测试环境数据路径
test_dir = os.path.join(configs_dir, 'test.conf')
# 日志配置路径
log_conf_dir = os.path.join(configs_dir, 'log.conf')


# common文件目录
commons_dir = os.path.join(base_dir, 'commons')

# 测试结果目录
result_dir = os.path.join(base_dir, r'results')
# logs结果存放目录
log_dir = os.path.join(result_dir, 'logs')
# 测试报告结果存放目录
report_dir = os.path.join(result_dir, 'reports')

# 测试用例目录
case_dir = os.path.join(base_dir, 'test_case')

# 测试数据目录
data_dir = os.path.join(base_dir, 'test_data', 'cases.xlsx')


