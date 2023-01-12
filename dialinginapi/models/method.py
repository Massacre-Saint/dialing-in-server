"""Module creates class Method"""
from django.db import models

class Method(models.Model):
    """Class defines Django Model of Method"""
    photo_url = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    dose_min = models.PositiveIntegerField()
    dose_max = models.PositiveIntegerField()
    weight_max = models.PositiveIntegerField()
