from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),    
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact')
]
