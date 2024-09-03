from rest_framework import serializers

from .models import Task, TaskSolutions


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'content', 'author', 'source', 'answer', 'topic', 'time_create', 'difficulty_level',
                  'is_available_in_bank', 'time_update')



class TaskSerializerForUser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'content', 'author', 'source', 'answer', 'topic', 'time_create', 'difficulty_level',
                  'time_update')
        fields = ('id', 'content', 'author')
        depth = 2


class TaskSolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSolutions
        fields = '__all__'
