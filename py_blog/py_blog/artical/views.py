# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponseRedirect

from models import Article
from models import Comment

# Create your views here.
def add(request):
    
    if request.method == 'POST':
        print "enter POST"
        # 获取POST提交的内容
        content = request.POST.get('content',None)
        title = request.POST.get('title',None)
        new = Article(content=content,title=title)
        new.save()
        # 请求重定向
        return HttpResponseRedirect('/list')
    print "enter GET"
    # POST提交方式中需要使用render方法才能正常工作
    return render(request,'add.html',{'method_str':request.method})

def list(request):
    # ORM方式查询数据
    articles = Article.objects.order_by("-id").all()
    return render_to_response('list.html',{'articles':articles})

def view(request,id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(Article=id).order_by("-id").all()
    return render(request,'view.html',{'article':article,'comments':comments})

def comment_add(request):
    
    if request.method == 'POST':
        article_id = request.POST.get('article','')
        detail = request.POST.get('detail','')
        if article_id and detail:
            comment = Comment()
            comment.Article = Article(id=article_id)
            comment.detail = detail
            comment.save()

    return HttpResponseRedirect('/view/%s'%article_id)