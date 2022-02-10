from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^fontpage/$', views.FontPage.as_view(success_url='/'), name='fontpage'),
    url(r'^about/',views.About.as_view(success_url='/'),name='about'),
    url(r'^archives',views.Archives.as_view(success_url = '/'),name='archives'),
    url(r'^blog',views.Blog.as_view(success_url= '/'),name='blog'),
    url(r'^tags',views.Tags.as_view(success_url = '/'),name = 'tags'),
    url(r'^types',views.Types.as_view(success_url = '/'),name = 'types'),
    url('polls_Blog',views.polls_Blog)

]