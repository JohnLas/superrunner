# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.races, name='home'),
    url(r'race/(?P<id_race>[0-9]*)$', views.race, name='race'),
    url(r'races', views.races, name='races'),
    url(r'map', views.map, name='map'),
]
