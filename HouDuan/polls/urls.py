from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^fontpage/$', views.FontPage.as_view(success_url='/'), name='fontpage'),
    url(r'^about/',views.About.as_view(success_url='/'),name='about'),
]