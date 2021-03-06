"""RepastSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# from django.conf.urls import include, url
# from django.contrib import admin
# from RepastSystem.view import hello
#
# urlpatterns = [
#     url(r'^hello/$', hello),
#     # url(r'^admin/', include(admin.site.urls)),
# ]

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from RepastSystem.view import *
from Human.views import *

# from oscar.app import application

from Books.views import BookListView
# from django.views.generic.list import ListView
# from django.views.generic import TemplateView
# from Books.models import *
#
# # book_info = {
# #     'queryset': Book.objects.all,
# #     'template_name': 'booklist.html'
# # }

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^myself/$', myselfweb),
    #  using template view, we no need to  realize views
    # ('^about/$', TemplateView.as_view(template_name='about.html')),
    # ('^booklist/$', ListView.as_view(**book_info)),
    ('^booklist/$', BookListView.as_view()),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # (r'^myweb/', include(application.urls)),
)

