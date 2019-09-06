#coding=utf-8
from django.http import HttpResponse

def home(request,num):
    return HttpResponse('hello,wonderful %s world!'%num)
