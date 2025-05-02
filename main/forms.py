from django import forms

from .models import Listing

class ListingForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = Listing
        fields = {
            'brand', 'engine', 'vin', 'mileage', 'description', 'transmisson', 'image','model'
        }