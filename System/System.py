#-*- coding:utf-8 -*-
# @Time    : 2017/5/25 05:31
# @Author  : Sml2h3
# @Site    : www.ydyd.me
# @File    : System.py
# @Software: PyCharm

from Control.Control import Control
from Config.Config import Server


class System(object):
    def __init__(self):
        self.char = Server['CHAR']
        self.control = Control()

    def run(self):
        if Server['CHAR'] == 'master':
            self.control._run()
