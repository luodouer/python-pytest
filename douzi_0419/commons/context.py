# encoding=utf-8
# @Author   ： 豆子
# @Function ：  上下文管理，正则替换

import re

from configparser import NoOptionError

from douzi_0419.commons import constant
from douzi_0419.commons.configpar import ConfigPar


class Context:
    a = None
    pwd_length_case_id = 1


class Replace:
    '''
    参数化替换
    '''

    @staticmethod
    def find_str(section, target):
        base_dir = constant.basedata_dir
        cp = ConfigPar(base_dir)
        pattern = '\${(.*?)}'
        while re.search(pattern, target):
            key = re.search(pattern, target).group(1)
            try:
                value = cp.get(section, key)
            except NoOptionError as a:
                if hasattr(Context, key):
                    value = getattr(Context, key)
                else:
                    raise a
            target = re.sub(pattern, value, target, count=1)
        return target


if __name__ == '__main__':
    a = '{"mobilephone":"${load_id}","pwd":"2222222","regname":"123"}'
    # pattern = '\${(.*?)}'
    # setattr(Context, 'load_id', '123')
    # print(re.search(pattern, a))
    p = Replace.find_str('data', a)
    print(p)
