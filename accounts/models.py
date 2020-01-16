from django.db import models
from django.contrib.auth.models import User


# class Project():
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=500)
#     start_time = models.DateField(blank=True)
#     end_time = models.DateField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
# class ProfileManager(models.Manager):
#     def validate_user(self, postData):
#         errors = {}
#         if len(postData['bio']) < 50:
#             errors['bio'] = "You have " + len(postData['bio']) + " characters left to type"
#         if len(postData['location']) < 1:
#             errors['location'] = "Please enter a value for city"
#         return errors
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     projects = models.ForeignKey(Project, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     profile_img = models.ImageField()
#
#
#
