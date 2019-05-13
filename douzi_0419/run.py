# encoding=utf_8
# @Author  ： 豆子

import sys

import pytest

from douzi_0419.commons import constant

sys.path.append('./')

pytest.main(['--html=resultss/reports/report.html', '--junitxml=resultss/reports/report.xml', '-m', 'register', '--reruns', '2',
    '--alluredir=resultss/allure'])