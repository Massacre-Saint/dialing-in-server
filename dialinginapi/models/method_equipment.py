"""Module defines class Method Equipment"""
from django.db import models
from .method import Method

class MethodEquipment(models.Model):
    """CLass defines Django Model of Method Equipment"""
    type = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
