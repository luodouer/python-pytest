# encoding=utf_8
# @Author   ： 豆子
# @Function :  不同测试环境配置文件读取


from douzi_0419.commons import constant
from douzi_0419.commons.configpar import ConfigPar


class TestEnSwitch(ConfigPar):
    def __init__(self):
        filename = constant.global_dir
        super(TestEnSwitch, self).__init__(filename)
        if self.getboolean('switch', 'on'):
            online = constant.online_dir
            super(TestEnSwitch, self).__init__(online)
        else:
            test = constant.test_dir
            super(TestEnSwitch, self).__init__(test)


if __name__ == '__main__':
    s = TestEnSwitch()
    a = s.get('api', 'url')
    print(a)
    print(type(a))
