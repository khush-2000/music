from . import views
from django.conf.urls import url

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),

    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
