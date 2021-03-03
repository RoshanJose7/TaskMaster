from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TaskList(models.Model):
	list_title = models.CharField(max_length=25, unique=True)
	created_at = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Name: {self.list_title}\nCreated At: {self.created_at}"

class Task(models.Model):
	task_title = models.CharField(max_length=25, unique=True)
	description = models.CharField(max_length=256)
	due_date = models.DateTimeField()
	task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)