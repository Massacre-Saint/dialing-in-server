"""Module creates class Recipe"""
from django.db import models
from .grind import Grind
from .method import Method


class Recipe(models.Model):
    """Defining Django Model of Recipe"""
    brew_time = models.PositiveIntegerField(null=True)
    grind_id = models.ForeignKey(Grind, on_delete= models.CASCADE, null=True)
    weight = models.PositiveIntegerField(null=True)
    dose = models.PositiveIntegerField(null=True)
    method_id = models.ForeignKey(Method, on_delete= models.CASCADE, null=True)
    recipe_name = models.CharField(max_length=35, null=True)
    default = models.BooleanField()
    published = models.BooleanField(null=True)
