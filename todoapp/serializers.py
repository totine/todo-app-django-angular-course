from rest_framework import serializers
from todoapp.models import ToDoElement


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoElement
        fields = ['id', 'todo_text', 'is_done']
