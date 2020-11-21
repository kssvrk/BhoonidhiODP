from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('createjob',views.create_job,name='create_job'),
    path('creategroup',views.create_group,name='create_group'),
    path('createprocess',views.create_process,name='create_process'),
    path('groups',views.group_list,name='group_list'),
    path('process',views.process_list,name='process_list'),
    
    
]