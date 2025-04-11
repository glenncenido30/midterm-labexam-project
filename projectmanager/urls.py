from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:project_id>/task/create/', views.task_create, name='task_create'),
    path('register/', views.register, name='register'),
    path('task/update/<int:task_id>/', views.task_update, name='task_update'),
]
