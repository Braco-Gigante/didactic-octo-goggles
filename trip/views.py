from django.shortcuts import render, redirect
from trip.forms import BenefactorForm, TripForm, CostForm
from trip.models import Benefactor, Trip, Cost


def index(request):
    return render(request, 'trip/home.html')


def add_benefactor(request):
    if request.method == 'POST':
        form = BenefactorForm(request.POST)
        if form.is_valid():
            benefactor = form.save(commit=False)
            benefactor.save()
            return redirect('/')
    else:
        form = BenefactorForm()
    return render(request, 'trip/generic_form.html', {'form': form})


def edit_benefactor(request, pk):
    benefactor = Benefactor.objects.get(id=pk)

    if request.method == 'POST':
        form = BenefactorForm(request.POST, instance=benefactor)
        if form.is_valid():
            benefactor = form.save(commit=False)
            benefactor.save()
            return redirect('/')
    else:
        form = BenefactorForm(instance=benefactor)
    return render(request, 'trip/generic_form.html', {'form': form})


def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.benefactor = Benefactor.objects.get(
                name=request.user.username)
            trip.save()
            return redirect('/')
    else:
        form = TripForm()
    return render(request, 'trip/generic_form.html', {'form': form})


def edit_trip(request, pk):
    trip = Trip.objects.get(id=pk)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('/')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trip/generic_form.html', {'form': form})


def add_cost(request, trip_pk):
    if request.method == 'POST':
        form = CostForm(request.POST, request.FILES)
        if form.is_valid():
            cost = form.save(commit=False)
            cost.trip = Trip.objects.get(pk=trip_pk)
            cost.save()
            return redirect('/')
    else:
        form = CostForm()
    return render(request, 'trip/generic_form.html', {'form': form})


def edit_cost(request, pk):
    cost = Cost.objects.get(id=pk)

    if request.method == 'POST':
        form = CostForm(request.POST, request.FILES, instance=cost)
        if form.is_valid():
            cost = form.save(commit=False)
            cost.save()
            return redirect('/')
    else:
        form = CostForm(instance=cost)
    return render(request, 'trip/generic_form.html', {'form': form})
