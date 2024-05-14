from django.db import models


class Task(models.Model):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    PRIORITY_CHOICES = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (MEDIUM, "High"),
    )
    description = models.CharField(max_length=128, help_text="Task description")
    priority = models.CharField(max_length=9, choices=PRIORITY_CHOICES, help_text="Task priority", default="Low", blank=True, null=True)
    estimation = models.FloatField(help_text="Task estimation in hours", default=0.0, blank=True, null=True)

class Car(models.Model):
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    price = models.FloatField()
    mileage = models.FloatField(default=0.0, blank=True, null=True)
