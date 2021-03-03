from trello.views import create_task, display_task_lists, create_task_list
from django.urls import path

urlpatterns = [
	path('', display_task_lists, name="display_task_lists"),
	path('list/add/', create_task_list, name="create_task_list"),
	path('task/add/', create_task, name="create_task")
]
