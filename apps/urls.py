# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'apps.view',
    url('^$', 'index.index', name='index'),
    url(r'^login/$','login_view.login', name = 'login'),
    url(r'^regist/$','login_view.regist', name = 'regist'),
    url(r'^logout/$','login_view.logout', name = 'logout'),

)