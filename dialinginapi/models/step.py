"""Module creates class Steo"""
from django.db import models
from .recipe import Recipe

class Step(models.Model):
    """Class defines DJango ORM model Step"""
    description = models.CharField(max_length=250)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
