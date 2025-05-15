
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('navbar/',views.navbar,name='navbar'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),

   path('tasks/',views.task_details,name='task_details'),
    path('add/',views.add_task,name='add_task'),
    path('delete/<int:task_id>/',views.delete_task,name='delete_task'),
    path('finished/<int:task_id>/',views.mark_finished,name='mark_finished'),
    path("edit/<int:task_id>/",views.edit_task, name="edit_task"),
]