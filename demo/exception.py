#coding:utf-8
import sys
import logging
import urllib

log = logging.getLogger()

logHandler = logging.FileHandler('/PythonProject/demo/log.txt')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logHandler.setFormatter(formatter)

log.addHandler(logHandler)

log.setLevel(logging.NOTSET)

try:
    a=3
    assert a == 4,'number not equals 4'
except:
    exc = sys.exc_info()
    # print exc[1]
    # print exc
    logging.error(exc[1])
# with 语句
with open('log.txt','r') as log:
    e = log.read()
    print e
# 自定义可供with调用的类
class sth(object):

    def __init__(self,name):
        print u"初始化了" 
        self.name = name
    def __enter__(self):
        print u"进入了"
        return self.name #返回可供操作的对象
    def __exit__(self,type,value,traceback):
        print u"跳出了"
with sth('bybe') as s: #得到__enter__方法返回的可操作对象
    print s

 #自定义异常类
class mException(Exception):

     def __init__(self,error,msg):
         self.args = (error,msg)
         self.error = error
         self.msg = msg
try:
    raise mException(1,'a new except')
except Exception as e:
    logging.debug(e)                   