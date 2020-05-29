from django import forms

from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'name', 'town', 'email', 'number','age','terms'
        ]

