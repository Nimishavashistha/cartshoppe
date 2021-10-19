from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('signup',views.signup,name="signup"),
    path('login',views.login)
]