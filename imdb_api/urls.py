from django.conf.urls import re_path, include
from django.contrib import admin
from Movies import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^$', views.index, name="index"),

    re_path(r'^movies/', include('Movies.urls')),

    re_path(r'^register/$', views.register, name="register"),

    re_path(r'^logged_in/$', views.logged_in, name="logged_in"),

    re_path(r'^logged_out/$', views.log_out, name="log_out"),

    re_path(r'^search/$', views.search_movie, name="search"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
