from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListPost.as_view(), name='all_post_url'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update_post_url'),
    path('category/', ListCate.as_view(), name='cate_list_url'),
    path('category/<int:pk>/', DetailCate.as_view(), name='cate_detail_url'),
    path('category/<int:pk>/<int:pke>/', DetailPodCate.as_view(), name='podcate_detail_url'),
    path('create/', ListCreateCate.as_view(), name='cate_post_create_url'),
    path('create/<int:pk>/', CreateDetailCate.as_view(), name='podpost_create_url'),
    path('create/<int:pk>/<int:pke>/', PostCreate.as_view(), name='post_create_detail_url'),
]
