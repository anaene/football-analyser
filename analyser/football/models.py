from django.db import models


# Create your models here.
class Confederation(models.Model):
    abbreviation = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.abbreviation


class Association(models.Model):
    name = models.CharField(max_length=50, unique=True)
    confederation = models.ForeignKey(Confederation, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
