from django import forms
from .models import *

class CreateForm(forms.Form):
    name = forms.CharField(
            label='name',
            max_length=100,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'event name',
                    'autofocus': ''}))

    info = forms.CharField(
        label='info',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'event info'}))


    location = forms.CharField(
        label='info',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'location info'}))

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'mm/dd/yyyy',
                'type': 'date', 'class': 'form-control' }))

    start_time = forms.TimeField(input_formats=['%I:%M %p', '%H:%M'], widget=forms.TimeInput(
        attrs={'placeholder': '--:-- --  i.e. 10:00 AM', 'type': 'time', 'class': 'form-control'}))

    end_time = forms.TimeField(input_formats=['%I:%M %p', '%H:%M'], widget=forms.TimeInput(
        attrs={'placeholder': '--:-- --  i.e. 06:30 PM', 'type': 'time', 'class': 'form-control'}))
