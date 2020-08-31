# from  django.conf.urls import url

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^query1$', views.query1, name='query1'),
    re_path(r'^queryresult1$', views.queryresult1, name='queryresult1'),
    re_path(r'logsnewcontent$', views.logsnewcontent, name='logsnewcontent'),
    re_path(r'logsnewcontent1$', views.logsnewcontent1, name='logsnewcontent1'),
    re_path(r'logsformat$', views.logsformat, name='logsformat'),
    re_path(r'logsformatForm$', views.logsformatForm, name='logsformatForm'),
    re_path(r'^downfile/$', views.downfile,name='downfile'),
]

