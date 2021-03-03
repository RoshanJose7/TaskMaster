from trello.models import Task
from django import forms

class CreateTaskForm(forms.ModelForm):
	class Meta():
		model = Task
		fields = ['task_title', 'description', 'due_date', 'task_list', 'owner']

		widgets = {
			'due_date' : forms.DateTimeInput(attrs={'type' : 'datetime-local'}),
			'description' : forms.Textarea()
		}		