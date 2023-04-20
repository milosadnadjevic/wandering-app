from django.forms import ModelForm
from .models import Restaurant, Attraction

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'restaurant_des', 'restaurant_url')


class AttractionForm(ModelForm):
    class Meta:
        model = Attraction
        fields = ('attraction_name', 'attraction_description', 'attraction_url')