"""zwhk_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from zwhk_blog.admin_site import admin_site
from django.conf import settings
from django.conf.urls.static import static
from zwhk_blog.feeds import DjangoBlogFeed

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
handle403 = 'blog.views.permission_denied_view'

urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'',include('blog.urls',namespace='blog')),
    url(r'', include('accounts.urls', namespace='account')),
    url(r'', include('oauth.urls', namespace='oauth')),
    url(r'', include('comments.urls', namespace='comment')),
    
    #simditor
    url(r'^simditor/', include('simditor.urls')),
    #Search
    url(r'^search', include('haystack.urls'), name='search'),
    #RSS
    url(r'^feed/$', DjangoBlogFeed(), name='feed'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)