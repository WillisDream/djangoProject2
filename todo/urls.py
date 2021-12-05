from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name="index"),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<str:task_id>/', views.update_post, name='update_product'),
    path('delete/<str:task_id>/', views.delete, name="delete"),
path('complete/<str:task_id>/', views.complete, name="complete"),
]