"""Module creates class Owner"""
from django.db import models
from .recipe import Recipe
from .user import User

class Owner(models.Model):
    """Class defined Django Model ORM of Owner"""
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
