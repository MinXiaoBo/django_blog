# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'page/<int:page>/', views.IndexView.as_view(), name='index_page'),

    path(r'article/<int:year>/<int:month>/<int:day>/<int:article_id>.html',
         views.ArticleDetailView.as_view(),
         name='detailbyid'),

    path(r'record/<int:year>-<int:month>-<int:day>.html',views.RecordView.as_view(),
         name='record'),

    path(r'category/<slug:category_name>.html', views.CategoryDetailView.as_view(), name='category_detail'),
    path(r'category/<slug:category_name>/<int:page>.html', views.CategoryDetailView.as_view(),
         name='category_detail_page'),

    path(r'author/<author_name>.html', views.AuthorDetailView.as_view(), name='author_detail'),
    path(r'author/<author_name>/<int:page>.html', views.AuthorDetailView.as_view(),
         name='author_detail_page'),

    path(r'tag/<slug:tag_name>.html', views.TagDetailView.as_view(), name='tag_detail'),
    path(r'tag/<slug:tag_name>/<int:page>).html', views.TagDetailView.as_view(), name='tag_detail_page'),
    path('archives.html', views.ArchivesView.as_view(), name='archives'),

    path('parent_archives.html', TemplateView.as_view(template_name='blog/article_archives.html'), name='parent_archives'),

    path(r'upload', views.fileupload, name='upload'),
    path(r'refresh', views.refresh_memcache, name='refresh')
]
