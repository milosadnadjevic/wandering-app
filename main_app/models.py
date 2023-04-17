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