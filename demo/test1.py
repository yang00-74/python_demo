# -*- coding:utf-8 -*-
__all__ = ['func']
# x = 0
# while x < 100:
#     x += 1
#     print x
# else:
#     print 'count end'
for i in "i am a little children".split(' ') :
    print i,
    if len(i) > 3:
        print "more than 3" 
# for 最后一个遍历的值将被保留
else:
    print i

# 按照原本顺序输出字符串中出现过的字符
a = "AdmlkjjghgfgfaA"
a_list = list(a) # 转化为list，以便标记index用于排序
set_list = list(set(a_list))   #list转化为set去重，再转化为list排序
set_list.sort(key=a_list.index) #根据之前的list的下标排序
print ''.join(set_list)

key_list = []
dic = {'name':1,'use':8,'id':8}
for x,y in dic.items():
    if y == 8:
        key_list.append(x) #根据value获取key
    print x,y
print key_list

#全局字符串替换，
import string
q = '123456123421'
g = string.maketrans('12','ac') #翻译表方式，字符对应，12-ac， 21-ca
print q.translate(g) # translate(g,'2') 第二个参数为需要删除的每一个字符
print q.replace('12','ac') #匹配式 12-ac 21无法对应ca
def templateFunction(args):
    return args == 0
# print help(templateFunction.__code__) #查看方法元数据
print templateFunction.__code__.co_varnames #查看方法参数列表
print templateFunction.__code__.co_filename #查看方法所在文件

add = lambda x:x+1 if x > 0 else "error"
print add(2)
print add(-1)

p=filter(lambda x:x>'4',q) #过滤字符
print p

def func(a,b,c,d=4,*zoon,**room):
    return zoon,room
# print func(1,2,3,k=12,p=25,6,1,2,{4:5,6:7}) #报错 无键参数在有键参数之前
# func(d=4,a,b,c,*zoon,**room): #报错，无默认值参数在有默认值参数之后
print func(1,2,3,6,1,2,{4:5,6:7},k=12,p=25)

# 类结构中，任何方法至少要有self参数
class person(object):
    a = 1
    def __init__(self): #构造方法
        self.a = 2
    def __del__(self): #析构方法
        del self.a
p = person()
print p.a
    