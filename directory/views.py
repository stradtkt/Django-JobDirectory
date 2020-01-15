from django.shortcuts import render

from .models import *

def index(request):
    context = {}
    return render(request, 'directory/index.html', context)

def directory(request, id):
    context = {}
    return render(request, 'directory/directory.html', context)

def add_directory(request):
    if request.method == "POST":
        return
    else:
        context = {}
        return render(request, 'directory/add-directory.html', context)

def edit_directory(request, id):
    if request.method == "POST":
        return
    else:
        directory = Directory.objects.get(id=id)
        context = {
            "directory": directory
        }
        return render(request, 'directory/edit-directory', context)