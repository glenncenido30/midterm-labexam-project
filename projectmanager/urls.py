from django.urls import path
from . import views
from projectmanager.views import project_update
from projectmanager.views import project_delete
from projectmanager.views import task_delete



urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:project_id>/task/create/', views.task_create, name='task_create'),
    path('register/', views.register, name='register'),
    path('task/update/<int:task_id>/', views.task_update, name='task_update'),
    path('project/<int:project_id>/update/', project_update, name='project_update'),
    path('project/<int:project_id>/delete/', project_delete, name='project_delete'),
    path('task/delete/<int:task_id>/', task_delete, name='task_delete'),

]
