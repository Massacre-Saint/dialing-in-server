"""Module creates class Grind"""
from django.db import models

class Grind(models.Model):
    """Class defines Django Model of Grind"""
    grind_size = models.CharField(max_length=50)
    image_url = models.CharField(max_length=150)
    order = models.PositiveIntegerField()
  