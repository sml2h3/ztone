#-*- coding:utf-8 -*-
# @Time    : 2017/5/25 08:46
# @Author  : Sml2h3
# @Site    : www.ydyd.me
# @File    : ApiGetIp.py
# @Software: PyCharm
import requests
import time
from Logger.Logger import Logger
from ProxyValidate import ProxyValidate
import threading


class ApiGetIp(object):
    def __init__(self, apiurl, username="", password="", split="\r\n", other={}):
        self.apiurl = apiurl
        self.username = username
        self.password = password
        self.split = split
        self.other = other
        self.open = True
        self.valide = ProxyValidate()
        self.log = Logger('ApiGetIp')

    def run(self):
        while(self.open):
            self.log.info("正在从代理API获取代理IP")
            try:
                result = requests.get(self.apiurl, headers=self.other)
            except requests.RequestException as error:
                self.log.error("API访问失败，原因为"+error)
                time.sleep(5)
                continue
            if result.status_code == 200:
                result_text = result.text
                ip_list =result_text.split(self.split)
                self.log.info("本次从API处获取到的代理数量为"+str(len(ip_list))+"枚,即将进入有效性验证")
                threading.Thread(target=self.valide.check, args=((ip_list),)).start()
                time.sleep(20)
                continue
            else:
                self.log.warning("API接口似乎出现了一些问题，请检查后重试!错误码为"+str(result.status_code))
                time.sleep(5)
                continue

