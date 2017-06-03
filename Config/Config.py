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
    系统设置
        CHAR:角色设置
            master:主控机、crawler:数据抓取机、dataer:数据存储机
            默认为master

'''
Server = {
    "CHAR": "master",
}
'''
    代理池设置
        TYPE:代理类型
            api:通过其他网站提供的api获取代理ip、list:私有的代理ip列表、head:通过添加head代理头自动进行代理
'''
PROXY = {
    "TYPE": "api",
    "HTTP": "http://www.ip.cn/",
    "HTTPS": "https://www.baidu.com",
    "API": {
        "URL": "http://20686860202824048.standard.hutoudaili.com/?num=50&area_type=0&anonymity=0&order=1", #*
        "USERNAME": "",
        "PASSWORD": "",
        "SPLIT": "\r\n",
        "OTHER": {}
    },
    'VALIDATE_THREAD': 20,
    "LIST": [
        "127.0.0.1:8080"
    ],
    "HEAD": {
        "URL": "",
        "USERNAME": "",
        "PASSWORD": "",
        "OTHER": {}
    }
}
