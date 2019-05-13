# encoding=utf_8
# @Author   ： 豆子
# @Function :  配置文件解析


from configparser import ConfigParser


class ConfigPar:
    def __init__(self, filename):
        self.filename = filename
        self.cp = ConfigParser()
        self.cp.read(filenames=filename, encoding='utf-8')

    def has_section(self, section):
        '''
        :param section: 要查找的section
        :return: 存在，返回True，不存在，返回False
        '''
        if self.cp.has_section(section):
            return True
        else:
            return False

    def has_option(self, section, option):
        if self.cp.has_option(section, option):
            return True
        else:
            return False

    def get(self, section, option):
        return self.cp.get(section, option)

    def getint(self, section, option):
        return self.cp.getint(section, option)

    def getboolean(self, section, option):
        return self.cp.getboolean(section, option)

    def add_section(self, section):
        self.cp.add_section(section)

    def set(self, section, option, value):
        self.cp.set(section, option, value)
        with open(self.filename, 'w') as f:
            self.cp.write(f)


if __name__ == '__main__':
    # constant_dir = os.path.join(constant.configs_dir, 'test.conf')
    ConfigPar().get('api', 'url')
    a = ConfigPar().get('login', 'mobilephone')
    print(a)
    print(type(a))