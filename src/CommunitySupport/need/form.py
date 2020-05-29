from django import forms

from .models import Order, Donation

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'town', 'address', 'email', 'number', 'urgency', 'Non_Perishable', 'Perishable', 'terms'
        ]

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'name', 'town', 'address', 'email', 'number', 'donation', 'terms'
        ]

