from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.view_tasks),
    path("<int:task_id>", views.view_task),
    path("delete", views.delete_task),
]
