from django.shortcuts import render

class Trip:
    def __init__(self, destination, dates, hotel, hotel_link, img_url):
        self.destination = destination
        self.dates = dates
        self.hotel = hotel
        self.hotel_link = hotel_link
        self.img_url = img_url


trips = [
    Trip('Tulum', 'April 1st - April 10th', 'Casa Malca', 'https://www.booking.com', 'https://imgur.com/h3XTFBx'),
    Trip('Miami', 'May 1st - May 15', 'SLS', 'https://materializecss.com/cards.html', 'https://imgur.com/VdB5uKA'),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_trips(request):
    return render(request, 'my_trips.html', {'trips': trips})