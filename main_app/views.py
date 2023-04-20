from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip, Restaurant, Photo, Attraction
from .forms import RestaurantForm, AttractionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL='https://s3.us-east-1.amazonaws.com/'
BUCKET = 'wandering'

def home(request):
    return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

@login_required
def my_trips(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'my_trips.html', {'trips': trips})

@login_required
def trip_details(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    restaurant_form = RestaurantForm()
    attraction_form = AttractionForm()
    return render(request, 'detail.html', {'trip': trip, 'restaurant_form': restaurant_form, 'attraction_form': attraction_form})

@login_required
def add_restaurant(request, trip_id):
    form = RestaurantForm(request.POST)
    if form.is_valid():
        new_restaurant = form.save(commit=False)
        new_restaurant.trip_id = trip_id
        new_restaurant.save()
    return redirect('trip_details', trip_id=trip_id)

def add_attraction(request, trip_id):
    form = AttractionForm(request.POST)
    if form.is_valid():
        new_attraction = form.save(commit=False)
        new_attraction.trip_id = trip_id
        new_attraction.save()
    return redirect('trip_details', trip_id=trip_id)

@login_required
def delete_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    trip_id = restaurant.trip.id
    restaurant.delete()
    return redirect('trip_details', trip_id=trip_id)

@login_required
def delete_attraction(request, pk):
    attraction = Attraction.objects.get(pk=pk)
    trip_id = attraction.trip.id
    attraction.delete()
    return redirect('trip_details', trip_id=trip_id)

@login_required
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

def signup(request):
        error_message = ''
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('my_trips')
            else:
                error_message = 'Invalid Signup - try again'

        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form,  'error': error_message})

class TripCreate(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ('destination', 'dates', 'hotel', 'cover', 'hotel_url', 'hotel_description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ('destination', 'dates', 'hotel', 'hotel_url', 'hotel_description', 'cover')

class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'
    template_name = 'trips/trip_confirm_delete.html'


