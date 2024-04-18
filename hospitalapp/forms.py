from django import forms

from hospitalapp.models import Booking


class registrationForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'