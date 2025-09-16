from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('add/', views.add_todo, name='add_todo'),
    path('list/', views.list_todos, name='list_todos'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('complete/<int:todo_id>/', views.todo_complete, name='complete_todo'),
    path('delete/<int:todo_id>/', views.todo_delete, name='delete_todo'),
]