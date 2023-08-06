from django.db import models
from django.contrib import admin
class Student (models.Model):
    sid=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()

class StudentAdmin(admin.ModelAdmin):
    list_display=('sid','name','age','email')