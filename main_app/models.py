from django.db import models

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)
    cover = models.CharField(max_length=100)