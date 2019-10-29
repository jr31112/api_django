from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.index, name='index'),
    path('music/<int:music_pk>/', views.detail, name='detail')
]
