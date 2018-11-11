from django.shortcuts import render, redirect
from trip.forms import BenefactorForm, TripForm, CostForm


def index(request):
    return render(request, 'trip/home.html')


def benefactor(request):
    if request.method == 'POST':
        form = BenefactorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BenefactorForm()
    return render(request, 'trip/benefactor.html', {'form': form})


def trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CostForm()
    return render(request, 'trip/trip.html', {'form': form})


def cost(request):
    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal # noqa: E501
            # user.profile.university = form.cleaned_data.get('university')
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.profile.bio = form.cleaned_data.get('bio')
            # user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password) # noqa: E501
            # login(request, user)
            return redirect('/')
    else:
        form = CostForm()
    return render(request, 'trip/cost.html', {'form': form})
