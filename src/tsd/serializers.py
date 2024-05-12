from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    #description = serializers.CharField(help_text="description")

    class Meta:
        model = models.Task
        fields = '__all__'
