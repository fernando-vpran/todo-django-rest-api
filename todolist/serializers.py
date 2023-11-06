from rest_framework import serializers
from todolist.models import Task
 
class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'name',
                  'done')