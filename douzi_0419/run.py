# encoding=utf_8
# @Author  ： 豆子

import sys

import pytest

sys.path.append('./')
pytest.main(['--html=douzi_0419/Results/Reports/report.html', '--junitxml=douzi_0419/Results/Reports/report.xml', '-m', 'ff', '--reruns', '2',
    '--alluredir=douzi_0419/Results/allure'])