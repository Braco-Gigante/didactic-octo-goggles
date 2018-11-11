from django.shortcuts import render, redirect
from django.http import HttpResponse
from trip.forms import BenefactorForm, TripForm, CostForm
from trip.models import Benefactor, Trip, Cost


def index(request):
    return render(request, 'trip/index_user.html')

def index_adm(request):
    all_trips = Trip.objects.all()

    costs = Cost.objects.all()


    pie_graph_data = _get_cat_data(costs)

    context = { 'trips': all_trips,
                'pie_graph_data': pie_graph_data}

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
    trip_key = f"{trip.origin} ({trip.start}) --> {trip.destination} ({trip.end})"

    costs = Cost.objects.all().filter(trip=trip_key)

    total_spent = 0
    for cost in costs:
        total_spent += float(cost.value.replace(',', '.'))

    declared_limit = 2000
    percentage = int((total_spent / declared_limit) * 100)

    graph_data = _get_cat_data(costs)

    context = { 'trip': trip,
                'costs': costs,
                'total_spent': total_spent,
                'declared_limit': declared_limit,
                'percentage': percentage,
                'graph_data': graph_data}

    return render(request, 'trip/trip_single.html', context)



        # [{
        #     name: 'Chrome',
        #     y: 60
        # }, {
        #     name: 'Internet Explorer',
        #     y: 30
        # }, {
        #     name: 'Firefox',
        #     y: 10
        # }]


def add_cost(request):
    if request.method == 'POST':
        form = CostForm(request.POST, request.FILES)
        if form.is_valid():
            cost = form.save(commit=False)
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
