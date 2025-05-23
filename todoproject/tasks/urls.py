from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import  views
from .views import TaskViewSet

app_name = 'tasks'
router = DefaultRouter()
router.register('tasks', TaskViewSet)
urlpatterns = [
    path('',views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('api/', include(router.urls)),
]