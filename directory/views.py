from django.shortcuts import render
from .choices import salary_of_job, location_of_job, developerlevel, duration_of_job
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

def search(request):
    queryset_list = Directory.objects.order_by('-created')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)

    if 'skills' in request.GET:
        skills = request.GET['skills']
        if skills:
            queryset_list = queryset_list.filter(skills__icontains=skills)

    if 'salary' in request.GET:
        salary = request.GET['salary']
        if salary:
            queryset_list = queryset_list.filter(salary__lte=salary)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__icontains=location)

    if 'job_location' in request.GET:
        job_location = request.GET['job_location']
        if job_location:
            queryset_list = queryset_list.filter(job_location__exact=job_location)

    if 'developer_level' in request.GET:
        developer_level = request.GET['developer_level']
        if developer_level:
            queryset_list = queryset_list.filter(developer_level__exact=developer_level)

    if 'duration' in request.GET:
        duration = request.GET['duration']
        if duration:
            queryset_list = queryset_list.filter(duration__gte=duration)

    context = {
        "salary_of_job": salary_of_job,
        "location_of_job": location_of_job,
        "developerlevel": developerlevel,
        "duration_of_job": duration_of_job,
        "directories": queryset_list,
        "values": request.GET
    }
    return render(request, 'directory/search.html', context)

