from django.shortcuts import render
from .models import Project, CustomUser
from .forms import ProjectForm

# Create your views here.

def homeView(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm()
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'index.html', context)
