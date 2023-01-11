from django.db import models
from models import Method

class User(models.Model):
  uid = models.CharField(max_length=50)
  brew_method = models.ForeignKey(Method, on_delete=models.CASCADE)
  fav_roast = models.CharField(max_length=15)
  fav_shop = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  photo_url = models.CharField(max_length=150)
  name = models.CharField(max_length=50)
  
  
    