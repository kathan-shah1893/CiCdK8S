from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index,name="register"),
    path('insert', views.insert, name="register"),
    path('checklogin',views.login,name="checklogin"),
    path('login',views.logg,name="login"),
    path('dashbord',views.dashbord,name="dash"),
]