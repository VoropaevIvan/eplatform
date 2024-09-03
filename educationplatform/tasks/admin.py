from django.contrib import admin

from .models import Task, Author, TaskSource, DifficultyLevel, TaskTopic, TaskSolutions

admin.site.register(Task)
admin.site.register(Author)
admin.site.register(TaskSource)
admin.site.register(DifficultyLevel)
admin.site.register(TaskTopic)

admin.site.register(TaskSolutions)