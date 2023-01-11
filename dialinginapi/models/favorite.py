from django.db import models
from models import (
  Grind,
  Method,
  Process,
  User,
  UserRecipe,
  DefaultRecipe
)

class Favorite(models.Model):
  brew_time = models.PositiveIntegerField()
  grind = models.ForeignKey(Grind, on_delete= models.CASCADE)
  weight = models.PositiveIntegerField()
  dose = models.PositiveIntegerField()
  method = models.ForeignKey(Method, on_delete= models.CASCADE)
  process = models.ForeignKey(Process, on_delete= models.CASCADE)
  uid = models.ForeignKey(User, on_delete = models.CASCADE)
  recipe_name = models.CharField(max_length=35)
  water_temp = models.PositiveIntegerField()
  user_recipe = models.ForeignKey(UserRecipe, on_delete= models.CASCADE)
  default_recipe =  models.ForeignKey(DefaultRecipe, on_delete= models.CASCADE)
  completed = models.BooleanField()
