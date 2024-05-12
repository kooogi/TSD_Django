from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers, models


class TaskViewSet(viewsets.ModelViewSet):
    """
    Return information about task.
    """
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()



@api_view(['GET', 'POST'])
def first_endpoint(request):
    if request.method == 'GET':
        # Logic for handling GET requests
        return Response({"message": "This is a GET request"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Logic for handling POST requests
        return Response({"message": "This is a POST request"}, status=status.HTTP_201_CREATED)
