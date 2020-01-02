# coding=utf-8

import os
import time

# 项目路径
project_path = os.path.abspath('.')
# 日志路径
log_path = os.path.join(project_path,'report', 'logs','test_{}.log'.format(time.strftime('%Y-%m-%d')))
# 测试报告路径
report_path = os.path.join(project_path, 'report', 'html_report')
# 截图文件路径
img_path = os.path.join(report_path,'images')
# 默认浏览器
browser = 'Chrome'
# 是否开启静默模式,只有在chrome下支持开启
headless = False
# 测试数据路径
data_path = os.path.join(project_path, 'data', 'testdata')


print(report_path)
