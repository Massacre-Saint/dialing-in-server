"""Module creates class Recipe Equipment"""
from django.db import models
from .recipe import Recipe

class RecipeEquipment(models.Model):
    """Class defines Django Model Recipe Equipment"""
    type = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    setting = models.CharField(max_length=150)
