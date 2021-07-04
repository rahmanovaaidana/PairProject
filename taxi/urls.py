from django.urls import path
from .views import Taxi,Taxi1,Taxi2,Taxi3

urlpatterns = [
    path('',Taxi.as_view(), name='taxi'),
    path('1/',Taxi1.as_view(), name='taxi_1'),
    path('2/', Taxi2.as_view(), name='taxi_2'),
    path('3/',Taxi3.as_view(), name='taxi_3'),
]