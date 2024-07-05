from django.shortcuts import render, redirect
from .forms import CreateTaskForm

# Todo Homepage
def index(request):
    return render(request, 'index.html')

# Todo creation page
def create(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateTaskForm()
    
    return render(request, 'create.html', {'form': form})
