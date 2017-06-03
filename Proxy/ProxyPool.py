#-*- coding:utf-8 -*-
# @Time    : 2017/5/25 08:26
# @Author  : Sml2h3
# @Site    : www.ydyd.me
# @File    : ProxyPool.py
# @Software: PyCharm

from Config.Config import PROXY,WEB
from ApiGetIp import ApiGetIp
from flask import Flask


class ProxyPool(object):
    def __init__(self):
        self.type_arr = {
            'api': self.API,
            'list': self.LIST,
            'head': self.HEAD
        }
        self.type = PROXY['TYPE']
        # 初始化中控web系统的参数
        self.app = Flask(__name__)
        # 访问端口
        self.port = WEB['PORT']
        # 是否公开
        self.public = True if WEB['PUBLIC'] else False
        # 调试模式是否开启
        self.debug = True if WEB['DEBUG'] else False
        # 子域名信息
        self.serve_name = WEB['SERVER_NAME']
        # 是否开启报错模式
        self.display_error = True if WEB['ERROR_DISPLAY'] else False
        # 配置集合
        self.app.config.update(
            DEBUG=self.debug,
            SERVER_NAME=self.serve_name + ':' + self.port,
            host='0.0.0.0' if self.public else '',
            TRAP_HTTP_EXCEPTIONS=self.display_error
        )

        @self.app.route('/getIp')
        def getIp():
            return 'Hello world'

    def _run(self):
        # self.app.run()
        self.type_arr.get(self.type)()

    def API(self):
        apiurl = PROXY['API']['URL']
        username = PROXY['API']['USERNAME']
        password = PROXY['API']['PASSWORD']
        splitstr = PROXY['API']['SPLIT']
        other = PROXY['API']['OTHER']
        ApiGetIp(apiurl=apiurl, username=username, password=password, split=splitstr, other=other).run()

    def LIST(self):
        return

    def HEAD(self):
        return