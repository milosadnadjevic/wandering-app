from django.db import models
from django.urls import reverse

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)
    cover = models.CharField(max_length=1000)
    hotel_url = models.CharField(max_length=1000)
    hotel_description = models.TextField(max_length=400)

    def __str__(self):
        return self.destination
    
    def get_absolute_url(self):
        return reverse('trip_details', kwargs={'trip_id': self.id})
    

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_des = models.TextField(max_length=250)
    restaurant_url = models.CharField(max_length=500)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.restaurant_name