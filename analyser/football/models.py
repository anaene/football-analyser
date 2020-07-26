from django.db import models


# Create your models here.
class Confederation(models.Model):
    abbreviation = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
