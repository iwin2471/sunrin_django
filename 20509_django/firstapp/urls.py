from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'second/', views.second, name='second'),
    url(r'introduce/', views.intro, name='introduce'),
    url(r'study/', views.study, name='study'),
    url(r'google/', views.google, name='google'),

    ]
