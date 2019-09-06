# -*- coding:utf-8 -*-
import time
import sys

print time.time()
"""
 多行注释，可用于输出
"""
str="hello world 中"
a=1
b=2 
print(str.decode("utf-8").encode("gbk"))
if a==b:
    print("is true")
else:    
    print("is false")
f=open('test.txt','r') #1.open the file
content = f.read()#2.read the file content
dcontent = content.decode('utf-8')

#string concat
#  c="%s%s" %(a,b) #tuple
# '%(who)%(sex)' %{'who':'i','sex':'boy'} #dict
content = "{a}{b}".format(a=str,b=content)
# content = str + content
# c="".join([a,b])

print content[0:20].decode('utf-8').encode('gbk') #substring 0-20
print len(dcontent)
"""
#find() the string start index 
#use index()will throw exception if the string not exist
"""
print content.find('this') 
r = open('test1.txt','w')#write file
#r.write(content[20:40])
#sys.stdout = r
#help(time)
r.close();

li = [x for x in xrange(1,10)] #create a list rang(1,10)
n=(4,9) #小括号为元组，不可变
m=[1,8,6] #中括号为列表，可变
p={'yangye':2} #大括号为字典，无序，可变 p=dict('yangye'=2)
print li
p['yangye'] ='bybe'
print p
print set("yangye") #set集合无序可进行操作，frozenset不可操作

import test1 #导入自定义文件
print test1.func(1,2,3,6,1,2,{4:5,6:7},k=12,p=25)

# import model.testmodel as model
# from model import testmodel
from model import * #该用法需要配置模块下面的__init__.py文件的__all__=[]
print testmodel.getName('yangye')