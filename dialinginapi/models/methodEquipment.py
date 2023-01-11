from django.db import models
from models import Method

class MethodEquipment(models.Model):
  type = models.CharField(max_length=150)
  name = models.CharField(max_length=150)
  method = models.ForeignKey(Method, on_delete=models.CASCADE)
