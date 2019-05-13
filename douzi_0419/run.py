# encoding=utf_8
# @Author  ： 豆子

import sys

import pytest

sys.path.append('./')
pytest.main(['--html=douzi_0419/results/reports/report.html', '--junitxml=douzi_0419/results/reports/report.xml', '-m', 'register', '--reruns', '2',
    '--alluredir=douzi_0419/results/allure'])