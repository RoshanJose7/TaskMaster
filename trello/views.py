from trello.forms import CreateTaskForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import TaskList, Task

def display_task_lists(request):
	lists = TaskList.objects.all()
	tasks = Task.objects.all()
	return render(request, 'trello/display_task_list.html', { 'lists' : lists, 'tasks' : tasks})

@login_required(login_url='login')
def create_task_list(request):
	if request.method == "POST":
		list_title = request.POST['list_title']
		list = TaskList(list_title=list_title)
		list.save()

		return redirect('display_task_lists')
	else:
		return render(request, 'trello/create_task_list.html')

@login_required(login_url='login')
def create_task(request):
	if request.method == "POST":
		form = CreateTaskForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('display_task_lists')

	else:
		form = CreateTaskForm()
		return render(request, 'trello/create_task.html', {'form' : form})