from django.contrib import admin

# Register your models here.

from .models import Trip, Restaurant, Photo, Attraction
admin.site.register(Trip)
admin.site.register(Restaurant)
admin.site.register(Photo)
admin.site.register(Attraction)