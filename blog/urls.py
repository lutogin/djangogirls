from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^add-post', views.add_post, name='add_post')
]
