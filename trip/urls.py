from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_adm', views.index_adm, name='index_adm'),
    path('benefactor/', views.add_benefactor, name='benefactor'),
    path('benefactor/<pk>', views.edit_benefactor, name='cost'),
    path('trip/', views.add_trip, name='trip'),
    path('trip/edit/<pk>', views.edit_trip, name='cost'),
    path('trip/<pk>', views.trip_single, name='trip_single'),
    path('cost/', views.add_cost, name='cost'),
    path('cost/<pk>', views.edit_cost, name='cost'),
]
