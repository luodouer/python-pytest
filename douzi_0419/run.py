# encoding=utf_8
# @Author  ： 豆子

import sys

import pytest

sys.path.append('./')
pytest.main(['--html=Results/Reports/report.html', '--junitxml=Results/Reports/report.xml', '-m', 'ff', '--reruns', '2',
    '--alluredir=Results/allure'])