from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='user/logout.html'), name='user-logout'),

]
