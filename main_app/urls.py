from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.my_trips, name='my_trips'),
    path('trips/<int:trip_id>/', views.trip_details, name='trip_details'),
    path('trips/create/', views.TripCreate.as_view(), name='trip_create'),
]