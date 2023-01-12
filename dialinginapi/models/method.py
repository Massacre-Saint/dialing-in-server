"""Module creates class Method"""
from django.db import models

class Method(models.Model):
    """Class defines Django Model of Method"""
    image_url = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    dose_min = models.PositiveIntegerField(null=True)
    dose_max = models.PositiveIntegerField(null=True)
    weight_max = models.PositiveIntegerField(null=True)
