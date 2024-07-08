from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'due_date', 'details')
    search_fields = ('description', 'details')
    list_filter = ('status', 'due_date')
    ordering = ('due_date',)
