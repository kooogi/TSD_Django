from django.conf.urls import include
from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("tasks", views.TaskViewSet, "task")

urlpatterns = [
    re_path("", include(router.urls)),
    path('hello-world', views.first_endpoint),
]