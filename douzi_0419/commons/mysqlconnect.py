# encoding=utf-8
# @Author   ： 豆子
# @Function ： 数据库连接查询

import pymysql
from douzi_0419.commons.testenswitch import TestEnSwitch


class MySqlConnect:
    def __init__(self):
        cp = TestEnSwitch()
        host = cp.get('mysql', 'host')
        port = cp.getint('mysql', 'port')
        user = cp.get('mysql', 'user')
        pwd = cp.get('mysql', 'pwd')
        self.mysql = pymysql.connect(host=host, user=user, password=pwd, port=port)
        self.cur = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self, sql):
        self.mysql.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def fetch_all(self, sql):
        self.mysql.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.mysql.close()

    def commit(self):
        self.mysql.commit()


if __name__ == '__main__':
    sql = 'select MobilePhone from future.member where MobilePhone != "" ORDER BY MobilePhone DESC limit 1'
    mobile_phone=MySqlConnect().fetch_one(sql)
    print(mobile_phone)
    print(int(mobile_phone[0]) + 1)
