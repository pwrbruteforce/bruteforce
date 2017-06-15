from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'created', 'finished', 'status', 'hash', 'dictionary', 'max_password_len')
    list_filter = ('author','created', 'status','dictionary')


admin.site.register(Task, TaskAdmin)