from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListPost.as_view(), name='all_post_url'),
    path('category/', ListCate.as_view(), name='cate_list_url'),
    path('category/<pk>/', DetailCate.as_view(), name='cate_detail_url'),
    path('create/', ListCreateCate.as_view(), name='post_create_url'),
    path('create/<int:pk>/', PostCreate.as_view(), name='post_create_detail_url'),
]
