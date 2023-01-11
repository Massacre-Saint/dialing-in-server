from django.db import models
from models import UserRecipe, DefaultRecipe

class RecipeEquipment(models.Model):
  type = models.CharField(max_length=150)
  name = models.CharField(max_length=150)
  user_recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE)
  default_recipe = models.ForeignKey(DefaultRecipe, on_delete=models.CASCADE)
  setting = models.CharField(max_length=150)
