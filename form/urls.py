from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list, name='all_post_url'),
    path('category/', cate_list, name='cate_list_url'),
    path('category/<str:category>/', cate_detail, name='cate_detail_url'),
    path('create/', Post_create.as_view(), name='post_create_url'),
]