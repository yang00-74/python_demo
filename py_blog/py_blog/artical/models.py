# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

class Comment(models.Model):
    Article = models.ForeignKey(Article, related_name='article_comment')
    detail = models.TextField()
        
