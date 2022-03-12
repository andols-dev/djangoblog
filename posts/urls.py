from collections import namedtuple
from django.urls import path

from .views import posts_view, create_posts_view,detail_view,update_post_view,contactView,successView,delete_view,delete_comment_view

urlpatterns = [
    path('',posts_view, name='posts'),
    path('create/',create_posts_view, name='create_post'),
    path('details/<int:id>/', detail_view,name='details'),
    path('update/<int:id>/',update_post_view,name='update_post'),
    path('delete/<int:id>/', delete_view, name='delete'),
    path('delete/comment/<int:id>/', delete_comment_view, name='delete_comment'),

    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]
