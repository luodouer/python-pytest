# encoding=utf-8
# @Author   ： 豆子
# @Function ：
import pytest


@pytest.mark.ff
@pytest.mark.usefixtures('reg_class')
def test_fail(reg_class):
    reg_class['logger'].info(reg_class['section_name'])
    # assert False

