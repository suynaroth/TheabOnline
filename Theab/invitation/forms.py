from django import forms
from .models import Event, Guest

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
 
class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Guest Name'}),
        }

        

