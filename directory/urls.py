from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="directory"),
    url(r'^(?P<id>\d+)$', views.directory, name="job"),
]