from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('benefactor/', views.add_benefactor, name='benefactor'),
    path('benefactor/<pk>', views.edit_benefactor, name='cost'),
    path('trip/', views.add_trip, name='trip'),
    path('trip/<pk>', views.edit_trip, name='cost'),
    path('cost/', views.add_cost, name='cost'),
    path('cost/<pk>', views.edit_cost, name='cost'),
]
