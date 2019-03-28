from django.urls import path, include
from .views import *

app_name = 'form'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('context/', ContextList.as_view(), name='context-list'),
    path('context/<int:pk>/', ContextSelect.as_view(), name='context-select'),
    path('intent/<int:pk>', NewExample.as_view(), name='intent-select'),
    path('example/<int:pk>', ExampleList.as_view(), name='example-list'),
]
