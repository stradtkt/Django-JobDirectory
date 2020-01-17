# from django.db import models
# from django.contrib.auth.models import User
#
#
# class EducationManager(models.Manager):
#     def validate_education(self, postData):
#         errors = {}
#         if len(postData['degree_description']) < 50:
#             errors['degree_description'] = "You have " + len(postData['degree_description']) + " characters left"
#         return errors
#
#
#
# class Education(models.Model):
#     degree_type = models.CharField(max_length=200, blank=True)
#     degree_title = models.CharField(max_length=True, blank=True)
#     degree_start_date = models.DateField(blank=True)
#     degree_end_date = models.CharField(blank=True)
#     degree_description = models.TextField(max_length=500, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     objects = EducationManager()
#
#     class Meta:
#         ordering = ['degree_start_date']
#
#     def __str__(self):
#         return self.degree_title
#
#
# class ExperienceManager(models.Manager):
#     def validate_experience(self, postData):
#         errors = {}
#         if len(postData['exp_description']) < 50:
#             errors['degree_description'] = "You have " + len(postData['exp_description']) + " characters left"
#         return errors
#
#
# class Experience(models.Model):
#     exp_title = models.CharField(max_length=200, blank=True)
#     exp_description = models.TextField(max_length=500, blank=True)
#     objects = ExperienceManager()
#
#
# class Project():
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=500)
#     project_img = models.ImageField()
#     start_time = models.DateField(blank=True)
#     end_time = models.DateField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['start_time']
#
#     def __str__(self):
#         return self.title
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
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
#     projects = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
#     exp = models.ForeignKey(Experience, on_delete=models.DO_NOTHING)
#     edu = models.ForeignKey(Education, on_delete=models.DO_NOTHING)
#     bio = models.TextField(max_length=500, blank=True)
#     developer_level = models.CharField(max_length=200, default='Entry')
#     github_link = models.CharField(max_length=200, blank=True)
#     linkedin_link = models.CharField(max_length=200, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     profile_img = models.ImageField()
#     objects = ProfileManager()


