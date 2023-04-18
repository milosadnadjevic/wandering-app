from django.contrib import admin

# Register your models here.

from .models import Trip, Restaurant
admin.site.register(Trip)
admin.site.register(Restaurant)