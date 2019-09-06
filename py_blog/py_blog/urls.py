#coding=utf-8
"""py_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views
import py_blog.artical.views as blog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
# 带括号表示请求所带的参数，<>内为参数名称
    url(r'^(?P<num>[\d]+)$',views.home),

    url(r'^add/$',blog.add),
    url(r'^list/$',blog.list),
    url(r'^view/(?P<id>[\d]+)$',blog.view),
    url(r'^comment/add/$',blog.comment_add),
]
