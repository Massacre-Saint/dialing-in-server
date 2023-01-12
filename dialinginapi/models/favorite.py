"""Module creates class Favorite"""
from django.db import models
from .recipe import Recipe
from .user import User

class Favorite(models.Model):
    """Defining Django Model of Favorite"""
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
