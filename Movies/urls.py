from django.conf.urls import re_path
from Movies import views, api
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'Movies'

urlpatterns = [

    re_path(r'^(?P<movie_id>[0-9]+)/$', views.detail, name="detail"),

    re_path(r'^(?P<movie_id>[0-9]+)/play/$', views.Play_movie, name="play"),

    re_path(r'^(?P<movie_id>[0-9]+)/watched/$', views.Watched, name="watched"),

    re_path(r'^(?P<movie_id>[0-9]+)/watched/stay=True$',
            views.Watched_stay, name="watched_stay"),

    re_path(r'^api/name=(?P<name>[A-Z,a-z," ",""]+|)?&y=(?P<year>[0-9]+|)$',
            api.API_res, name="api"),
]
