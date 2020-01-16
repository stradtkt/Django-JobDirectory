from django.shortcuts import render
from directory.models import Directory

def index(request):
    jobs = Directory.objects.all().order_by('-created')[0:3]
    context = {
        "jobs": jobs
    }
    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')
