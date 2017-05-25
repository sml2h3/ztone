#-*- coding:utf-8 -*-
# @Time    : 2017/5/25 04:03
# @Author  : Sml2h3
# @Site    : www.ydyd.me
# @File    : Config.py.py
# @Software: PyCharm

WEB = {
    "PORT": "8080",
    #中控网站的登录端口
    "PUBLIC": False,
    #中控系统是否运行在公网中，默认FALSE为关闭状态，TRUE为开启状态
    "SERVER_NAME": "127.0.0.1",
    #当PUBLIC为TRUE时，SERVER_NAME为用来访问的域名，如果不用域名访问，则保持默认即可
    "DEBUG": True,
    #调试模式
    "ERROR_DISPLAY": True
    #HTTP 异常的错误处理，而是像对待其它异常一样， 通过异常栈让它冒泡地抛出。这对于需要找出 HTTP 异常源头的可怕调试情形是有用的。
}
'''
    系统角色
    参数说明：
        CHAR
            master:主控机、crawler:数据抓取机、dataer:数据存储机
            默认为master

'''
Server = {
    "CHAR": "master",
}
