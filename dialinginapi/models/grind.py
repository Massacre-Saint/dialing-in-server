from django.db import models

class Grind(models.Model):
  grind_size = models.CharField(max_length=50)
  photoUrl = models.CharField(max_length=150)
  order = models.PositiveIntegerField()
  