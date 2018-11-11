from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('benefactor/', views.benefactor, name='benefactor'),
    path('trip/', views.trip, name='trip'),
    path('cost/', views.cost, name='cost'),
]
