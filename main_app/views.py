from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip, Restaurant, Photo
from .forms import RestaurantForm
import uuid
import boto3

S3_BASE_URL='https://s3.us-east-1.amazonaws.com/'
BUCKET = 'wandering'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_trips(request):
    trips = Trip.objects.all()
    return render(request, 'my_trips.html', {'trips': trips})

def trip_details(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    restaurant_form = RestaurantForm()
    return render(request, 'detail.html', {'trip': trip, 'restaurant_form': restaurant_form})

def add_restaurant(request, trip_id):
    form = RestaurantForm(request.POST)
    if form.is_valid():
        new_restaurant = form.save(commit=False)
        new_restaurant.trip_id = trip_id
        new_restaurant.save()
    return redirect('trip_details', trip_id=trip_id)

def add_photo(request, trip_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            Photo.objects.create(url=url, trip_id=trip_id)
        except Exception as error:
            print('Photo upload failed')
            print((error))
    return redirect('trip_details', trip_id=trip_id)

    

class TripCreate(CreateView):
    model = Trip
    fields = ('__all__')

class TripUpdate(UpdateView):
    model = Trip
    fields = ('destination', 'dates', 'hotel', 'hotel_url', 'hotel_description', 'cover')

class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'
    template_name = 'trips/trip_confirm_delete.html'

def delete_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    trip_id = restaurant.trip.id
    restaurant.delete()
    return redirect('trip_details', trip_id=trip_id)
