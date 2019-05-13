# encoding=utf_8
# @Author   ： 豆子
# @Function :  http请求

import json
import requests
from douzi_0419.commons.testenswitch import TestEnSwitch


class TestHttpRequest:
    def __init__(self):
        self.session = requests.sessions.session()
        self.req = None

    def request(self, url, method, data=None, jsons=None, headers=None):
        method = method.lower()
        if isinstance(data, str):
            data = json.loads(data)
        url = TestEnSwitch().get('api', 'url') + url
        if method == 'get':
            self.req = self.session.request(url=url, method=method, params=data, json=jsons, headers=headers)
        elif method == 'post':
            self.req = self.session.request(url=url, method=method, data=data, json=jsons, headers=headers)
        else:
            pass
        # return self.req

    def get_json_code(self):
        return self.req.json()['code']

    def get_json(self):
        return self.req.json()

    def get_cookies(self):
        return self.req.cookies

    def get_text(self):
        return self.req.text

    def close(self):
        self.session.close()
