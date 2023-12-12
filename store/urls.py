from django.urls import path
from .views import *

urlpatterns = [
    path('',Store.as_view(),name='store'),
    path('BookDetail/<uuid:pk>/',Detail.as_view(),name='detail'),
    path('deletebook/<uuid:pk>/',Delete.as_view(),name='delete'),

]
