from django.contrib import admin

# Register your models here.
from .models import Task, Answers

admin.site.register(Task)
admin.site.register(Answers)
