# encoding=utf_8
# @Author   ： 豆子
# @Function :  账号注册


import pytest
from douzi_0419.commons.context import Replace, Context
from douzi_0419.commons import constant
from douzi_0419.commons.excelparse import ExcelParse

ep = ExcelParse(constant.data_dir)
cases = ep.get_cases('register')


@pytest.mark.register
@pytest.mark.usefixtures('reg_class')
@pytest.mark.usefixtures('reg_func')
class TestRegister:

    @pytest.mark.register
    @pytest.mark.parametrize('case', cases)
    def test_register(self, case, reg_class, reg_func):
        self.session = reg_class['session']
        self.logger = reg_class['logger']
        self.cp = reg_class['cp']
        self.mysql_connect = reg_class['mysql_connect']
        self.count_sql = reg_func['count_sql']
        self.phone = reg_func['phone']
        self.pwd = reg_func['pwd']
        self.section_name = reg_class['section_name']

        self.headers = reg_class['headers']

        case.data = Replace.find_str(self.section_name, case.data)
        try:
            self.session.request(url=case.url, method=case.method, data=case.data, headers=self.headers)
            assert str(case.expected) == self.session.get_json_code()
            new_user = self.mysql_connect.fetch_one(self.count_sql)['count']
            if self.session.get_json()['msg'] == '注册成功':
                self.cp.set(self.section_name, 'register_user_s', str(self.phone))
                self.cp.set(self.section_name, 'register_pwd_s', self.pwd)
                assert 1 == new_user
                self.logger.info('手机号码 {} 注册成功，对应手机号的登陆密码是：{}'.format(self.phone, self.pwd))
            else:
                assert 0 == new_user
            result = 'Pass'
        except AssertionError as a:
            self.logger.exception()
            result = 'Fail'
            raise a
        finally:
            self.logger.info('测试模块：{}，测试用例id：{}，测试目的：{}，请求响应结果：{}，执行结果：{}'.
                             format(case.sheet_name, case.case_id, case.title, self.session.get_text(), result))
            ep.back_write_by_excel(case.sheet_name, case.case_id, self.session.get_text(), result)
            setattr(Context, 'pwd_length_case_id', case.case_id + 1)


if __name__ == '__main__':
    pass
