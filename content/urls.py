from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'race/(?P<id_race>[0-9]*)$', views.race, name='race'),
    url(r'race/(?P<id_race>[0-9]*)/edition/(?P<id_edition>[0-9]*)$', views.edition, name='edition'),
    url(r'races', views.races, name='races'),
    url(r'runner/(?P<id_runner>[0-9]*)', views.runner, name='runner'),
    url(r'runners', views.runners, name='runners'),
    url(r'chrono/(?P<id_chrono>[0-9]*)', views.chrono, name='chrono'),
]