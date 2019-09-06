#coding=utf-8
import threading

mLock = threading.Lock()#锁对象
num = 0
def test():
    global num
    mLock.acquire() #加锁
    num += 1
    mLock.release() #放锁
    print num 

threadList = []
for i in xrange(0,10):
    a = threading.Thread(target=test)
    a.start()
    threadList.append(a)
# for a in threadList:
#     a.join() #调用join()的线程有优先运行的权限

print "run to end"

#协程 可将正在遍历的数据加载进一个可迭代对象返回，从而传递值
#根据 generator对象 next（），send（）方法进行流程控制,执行到yield 就不再执行
def count():
    i = 0
    while i < 5:
        x = yield 'the %s'%i
        print i
        i += 1
c = count()
print type(c)
# for i in c:
#     print i,
print c.next()
print c.send('modify')
print c.next()

def test():    
    x = yield u'第一步，他会直接返回'
    print u'哈哈，第一次赋值，%s'%x
    x = yield u'%s,它每次请求，不管是send，还是next，都会往下一直跑到下一个yield'%x
    print u'哈哈，第二次赋值，%s'%x
    x = yield u'会有第三次，%s'%x
t = test()
print t.next()
# print t.next()
# print t.next()
print t.send(u'赋值给第一个x！')
print t.send(u'给第二x个赋值')