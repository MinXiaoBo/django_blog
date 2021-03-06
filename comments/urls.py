#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: urls.py
@time: 2016/11/12 下午3:03
"""

from django.urls import path
from . import views

app_name = "comments"
urlpatterns = [
    path('article/<int:article_id>/postcomment', views.CommentPostView.as_view(), name='postcomment'),
]
