# encoding=utf_8
# @Author   ： 豆子
# @Function :  日志配置文件读取

import logging
from logging.handlers import TimedRotatingFileHandler
import os
from douzi_0419.commons import constant
from douzi_0419.commons.configpar import ConfigPar


class Logger(object):
    def __init__(self, log_name):
        cp = ConfigPar(constant.log_conf_dir)
        # 定义一个日志收集器
        self.logger = logging.getLogger(log_name)
        # 设置收集器的输出级别
        self.logger.setLevel(cp.get('root', 'level'))
        # famatter = logging.Formatter(cp.get('famatter', 'famatter'))
        famatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - 日志信息：%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(cp.get('stream', 'level'))
        ch.setFormatter(famatter)

        log_dir = os.path.join(constant.log_dir, cp.get('file', 'file'))
        fh = TimedRotatingFileHandler(filename=log_dir, encoding='utf-8', when='M', backupCount=3)
        fh.setLevel(cp.get('file', 'level'))
        fh.setFormatter(famatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def clear_handler(self):
        self.logger.handlers.clear()

    def debug(self, msg):
        self.logger.debug(msg)
        # self.clear_handler()

    def info(self, msg):
        self.logger.info(msg)
        # self.clear_handler()

    def error(self, msg):
        self.logger.error(msg, exc_info=True)
        # self.clear_handler()

    def warning(self, msg):
        self.logger.warning(msg)
        # self.clear_handler()

    def exception(self, msg=None):
        self.logger.exception(msg)
        # self.clear_handler()


if __name__ == '__main__':
    Logger().error('123')
