from django.contrib import admin
from django.urls import path,include
from  todolist import views
app_name='todolist'
urlpatterns = [
    path('home/',views.home,name='主页'),
    path('edit/',views.edit,name='编辑'),
    path('about/', views.about,name='关于'),
]