from django.shortcuts import render, redirect
from django.http import HttpResponse
from trip.forms import BenefactorForm, TripForm, CostForm
from trip.models import Benefactor, Trip, Cost
from datetime import datetime


def index(request):
    return render(request, 'trip/index_user.html')


def index_adm(request):
    all_trips = Trip.objects.all()

    # pie
    costs = Cost.objects.all()
    pie_graph_data = _get_cat_data(costs)

    # bar
    cities = Cost.objects.values_list('where', flat=True).distinct()

    values_dict = {}
    values = []
    for city in cities:
        try:
            values_dict[city] = Cost.objects.all().filter(where=city)
        except:
            values_dict[city] = 0.0

        aux = 0
        for value in values_dict[city]:
            aux += float(value.value.replace(',', '.'))
        values.append(aux)

    # series
    days = []
    values_per_month = [0 for x in range(12)]
    days_list = list(Cost.objects.values_list('when', flat=True))
    cost_list = list(Cost.objects.values_list('value', flat=True))
    for day in days_list:
        days.append(datetime.strptime(day, '%d/%m/%Y'))
    for i, day in enumerate(days):
        values_per_month[day.month-1] += values[i]

    context = {'trips': all_trips,
               'pie_graph_data': pie_graph_data,
               'cities': cities,
               'values': values,
               'values_pm': values_per_month,
               }

    return render(request, 'trip/index_adm.html', context)


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
                user=request.user)
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


def _get_cat_data(costs):
    total_spent = 0
    for cost in costs:
        total_spent += float(cost.value.replace(',', '.'))

    cat_sum = {}
    for cost in costs:
        if cost.category not in cat_sum:
            cat_sum[cost.category] = float(cost.value.replace(',', '.'))
        else:
            cat_sum[cost.category] += float(cost.value.replace(',', '.'))

    graph_data = []
    for cat, my_sum in cat_sum.items():
        my_data = {}
        my_data['value'] = str(my_sum/total_spent)
        my_data['cat'] = cat
        graph_data.append(my_data)

    return graph_data


def trip_single(request, pk):
    trip = Trip.objects.get(pk=pk)
    costs = Cost.objects.all().filter(trip=pk)

    total_spent = 0
    for cost in costs:
        total_spent += float(cost.value.replace(',', '.'))

    declared_limit = 2000
    percentage = int((total_spent / declared_limit) * 100)

    graph_data = _get_cat_data(costs)

    context = {'trip': trip,
               'costs': costs,
               'total_spent': total_spent,
               'declared_limit': declared_limit,
               'percentage': percentage,
               'graph_data': graph_data}

    return render(request, 'trip/trip_single.html', context)


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
