from rest_framework import serializers

from .models import Task, TaskSolutions


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'content', 'author', 'source', 'answer', 'topic', 'time_create', 'difficulty_level',
                  'is_available_in_bank', 'time_update')
        # depth = 1


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
        # depth = 1

# # My Serializer
# class TaskSerializer2(serializers.Serializer):
#     content = serializers.CharField()
#     author_id = serializers.IntegerField()
#     answer = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Task.objects.create(**validated_data)
