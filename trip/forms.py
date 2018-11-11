from django import forms
# from django.contrib.auth.models import User
from trip.models import Benefactor, Trip, Cost
from datetime import datetime


class BenefactorForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)

    class Meta:
        model = Benefactor
        fields = ['name', 'role']


class TripForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    start = forms.CharField(max_length=100)
    end = forms.CharField(max_length=100)
    expected_cost = forms.FloatField()

    class Meta:
        model = Trip
        fields = ['name', 'origin', 'destination', 'start', 'end']


class CostForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    where = forms.CharField(max_length=100)
    when = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)
    receipt = forms.ImageField()

    class Meta:
        model = Cost
        fields = ['name', 'description', 'where',
                  'when', 'category', 'value', 'receipt']
