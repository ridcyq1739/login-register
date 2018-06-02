from django.conf.urls import url
from django.contrib import admin
from login import views

app_name = 'login'
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
]