from django.contrib import admin

# Register your models here.

from .models import Trip, Restaurant, Photo
admin.site.register(Trip)
admin.site.register(Restaurant)
admin.site.register(Photo)