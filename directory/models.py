from django.db import models
from django.contrib.auth.models import User

class Directory(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    logo = models.ImageField(blank=True)
    description = models.TextField()
    salary = models.IntegerField()
    duration = models.IntegerField()
    location = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200)
    developer_level = models.CharField(max_length=200)
    skills = models.CharField(max_length=500, db_index=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Applied(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    directory = models.ForeignKey(Directory, on_delete=models.DO_NOTHING)
    salary = models.IntegerField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

