"""Module creates class Recipe"""
from django.db import models
from .grind import Grind
from .method import Method


class Recipe(models.Model):
    """Defining Django Model of Recipe"""
    brew_time = models.PositiveIntegerField()
    grind_id = models.ForeignKey(Grind, on_delete= models.CASCADE)
    weight = models.PositiveIntegerField()
    dose = models.PositiveIntegerField()
    method_id = models.ForeignKey(Method, on_delete= models.CASCADE)
    recipe_name = models.CharField(max_length=35)
    water_temp = models.PositiveIntegerField()
    default = models.BooleanField()
    published = models.BooleanField()
