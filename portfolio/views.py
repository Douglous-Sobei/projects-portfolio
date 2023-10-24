from django.shortcuts import render
from .models import Project
# from .forms import ProjectForm


def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})
