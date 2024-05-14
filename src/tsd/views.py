from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from . import serializers, models
from django.shortcuts import render
from .models import Task, Car  # assuming your model is named 'Task' and 'Car'
from .serializers import CarSerializer

def tasks_view(request):
    tasks = Task.objects.filter(estimation__gt=5)  # replace 'estimation' with your field name
    return render(request, 'tasks.html', {'tasks': tasks})

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

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    mileage_param = openapi.Parameter('mileage', openapi.IN_QUERY, description="mileage manual param", type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(request_body=CarSerializer, manual_parameters=[mileage_param])
    def create(self, request, *args, **kwargs):
        mileage = request.query_params.get('mileage', None)
        if mileage is not None:
            request.data['mileage'] = mileage
        return super().create(request, *args, **kwargs)
