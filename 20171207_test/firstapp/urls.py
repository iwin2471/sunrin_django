from django.conf.urls import url
from . import views

urlpatterns=[
        url(r'^$',views.post_list, name='post_list'),
        url(r'second/', views.second, name='second'),
        url(r'third/', views.thrid, name='third'),
        url(r'detail/', views.post_detail, name='detail'),
        url(r'post/edit/', views.post_edit, name="edit"),
        url(r'post/new/', views.post_new, name="new")
]
