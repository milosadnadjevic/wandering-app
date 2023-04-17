from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Trip

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_trips(request):
    trips = Trip.objects.all()
    return render(request, 'my_trips.html', {'trips': trips})

def trip_details(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'detail.html', {'trip': trip})

class TripCreate(CreateView):
    model = Trip
    fields = ('__all__')
