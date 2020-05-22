from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
	task = Task.objects.all()

	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('home')	

	context = {'task':task, 'form':form}

	return render(request, 'tasks/main.html', context)

def update(request, pk):
	item = Task.objects.get(id=pk)
	form = TaskForm(instance=item)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}		
	return render(request, 'tasks/update.html', context)	

def delete(request, pk):
	item = Task.objects.get(id=pk)
	
	item.delete()

	return redirect('home')