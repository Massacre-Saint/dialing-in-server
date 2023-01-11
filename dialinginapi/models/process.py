from django.db import models
from models import DefaultRecipe, UserRecipe

class Process(models.Model):
  default_recipe = models.ForeignKey(DefaultRecipe, on_delete=models.CASCADE)
  user_recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE)
