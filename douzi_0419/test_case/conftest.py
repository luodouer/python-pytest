# encoding=utf-8
# @Author   ： 豆子
# @Function ：


import pytest
from douzi_0419.commons import constant
from douzi_0419.commons.configpar import ConfigPar
from douzi_0419.commons.context import Context
from douzi_0419.commons.logprase import Logger
from douzi_0419.commons.mysqlconnect import MySqlConnect
from douzi_0419.commons.page import RandomChoice
from douzi_0419.commons.testrequest import TestHttpRequest

section_name = None
mysql_connect = None
logger = None
cp = None


@pytest.fixture(scope='class')
def reg_class():
    global section_name, mysql_connect, logger, cp
    session = TestHttpRequest()
    mysql_connect = MySqlConnect()
    section_name = 'data'
    cp = ConfigPar(constant.basedata_dir)
    if not cp.has_section(section_name):
        cp.add_section(section_name)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    logger = Logger(__name__)

    yield {'session': session,
           'section_name': section_name,
           'mysql_connect': mysql_connect,
           'logger': logger,
           'cp': cp,
           'headers': headers}

    session.close()
    mysql_connect.close()
    logger.clear_handler()


@pytest.fixture
def reg_func():
    global section_name, mysql_connect, logger, cp
    p = True
    while p:
        phone_sql = 'SELECT MobilePhone FROM future.member  WHERE MobilePhone !="" ORDER BY MobilePhone LIMIT 1'
        mobile_phone = mysql_connect.fetch_one(phone_sql)['MobilePhone']
        phone = int(mobile_phone) + RandomChoice.random_choice_one(1, 100000000)
        count_sql = 'SELECT COUNT(*) count FROM future.member WHERE MobilePhone="{}"'.format(phone)
        p = mysql_connect.fetch_one(count_sql)['count']

    logger.info('注册用例执行之前，{} 手机号尚未注册'.format(phone))
    pwd_length_case_id = getattr(Context, 'pwd_length_case_id')

    if pwd_length_case_id == 4:
        pwd = RandomChoice.random_more_str(5)
    elif pwd_length_case_id == 5:
        pwd = RandomChoice.random_more_str(19)
    elif pwd_length_case_id == 6:
        pwd = RandomChoice.random_more_str(6)
    elif pwd_length_case_id == 7:
        pwd = RandomChoice.random_more_str(18)
    else:
        pwd = RandomChoice.random_more_str(8)

    option_user = 'register_user'
    option_pwd = 'register_pwd'
    cp.set(section_name, option_user, str(phone))
    cp.set(section_name, option_pwd, pwd)
    yield {'phone_sql': phone_sql,
           'pwd': pwd,
           'pwd_length_case_id': pwd_length_case_id,
           'count_sql': count_sql,
           'phone': phone}
