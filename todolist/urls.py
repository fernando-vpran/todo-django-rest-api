from django.urls import include, re_path
from todolist import views 
 
urlpatterns = [ 
    re_path(r'^api/todolist$', views.task_list, name="task-list"),
    re_path(r'^api/todolist/(?P<pk>[0-9]+)$', views.task_detail, name="task-detail"),
    re_path(r'^api/todolist/status/(?P<status>(done|undone))$', views.tasks_by_status, name="tasks-by-status"),
]