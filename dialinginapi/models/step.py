from django.db import models
from models import UserRecipe, DefaultRecipe

class Step(models.Model):
  description = models.CharField(max_length=250)
  user_recipe = models.ForeignKey(UserRecipe, on_delete= models.CASCADE)
  default_recipe = models.ForeignKey(DefaultRecipe, on_delete= models.CASCADE)
  order = models.PositiveIntegerField()
