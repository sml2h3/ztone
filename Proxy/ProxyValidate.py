#-*- coding:utf-8 -*-
# @Time    : 2017/5/25 08:58
# @Author  : Sml2h3
# @Site    : www.ydyd.me
# @File    : ProxyValidate.py
# @Software: PyCharm
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from Logger.Logger import Logger
from Config.Config import PROXY
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ProxyValidate(object):
    def __init__(self):
        self.checkhttp = PROXY['HTTP']
        self.checkhttps = PROXY['HTTPS']
        self.validate_thread = PROXY['VALIDATE_THREAD']
        self.proxy = {
            'http': '',
            'https': ''
        }
        self.pool = Pool(self.validate_thread)
        self.log = Logger('ProxyValidate')
        self.validip = {}

    def check(self, iplist):
        self.log.info("进入代理ip检验可用性系统，本次共提交"+str(len(iplist))+"个IP")
        if(len(iplist) < 1):
            self.log.info('共计提交0个IP进行检验，本次检验自动结束')
            return
        result = self.pool.map(self.validate, iplist)
        self.log.info("检验ip可用性结束，本次共计检验合格代理IP数量为"+str(len(self.validip))+"个，即将存入代理池")

    def validate(self, ip):
        proxy = self.proxy
        proxy['http'] = 'http://'+ip
        proxy['https'] = 'http://'+ip
        http = False
        https = False
        # http validate
        try:
            result_http = requests.get(self.checkhttp, proxies=proxy, timeout=6)
        except Exception as e:
            return
        if result_http.status_code == 200:
            # http valid
            http = True
        try:
            result_https = requests.get(self.checkhttps, proxies=proxy, timeout=6, verify=False)
        except Exception as e:
            return
        if result_https.status_code == 200:
            # https valid
            https = True
        if http or https:
            if (self.validip.has_key(ip)):
                return
            else:
                self.validip[ip] = {
                    'http': http,
                    'https': https
                }
            return
        else:
            return
