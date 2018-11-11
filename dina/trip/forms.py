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
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    start = forms.DateTimeField(initial=datetime.now())
    end = forms.DateTimeField(initial=datetime.now())

    def __init__(self, *args, **kwargs):
        super(BenefactorForm, self).__init__(*args, **kwargs)
        self.fields['benefactor'] = forms.ModelChoiceField(
            queryset=Benefactor.objects.all(), required=True)

    class Meta:
        model = Trip
        fields = ['origin', 'destination', 'start', 'end', 'benefactor']


class CostForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    where = forms.CharField(max_length=100)
    when = forms.DateTimeField(initial=datetime.now())
    category = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)
        self.fields['trip'] = forms.ModelChoiceField(
            queryset=Trip.objects.all(), required=True)

    class Meta:
        model = Cost
        fields = ['name', 'description', 'where',
                  'when', 'category', 'value', 'trip']
