from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.my_trips, name='my_trips'),
    path('trips/<int:trip_id>/', views.trip_details, name='trip_details'),
    path('trips/create/', views.TripCreate.as_view(), name='trip_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trip_delete'),
    path('trips/<int:trip_id>/add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('restaurant/<int:pk>/delete/', views.delete_restaurant, name='delete_restaurant'),
]