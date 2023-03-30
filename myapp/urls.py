from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('edit/<int:id>/', views.editView, name='edit'),
    path('delete/<int:id>/', views.deleteView, name='delete'),
]
