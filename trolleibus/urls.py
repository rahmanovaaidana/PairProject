from django.urls import path
from .views import Trolleibus,Trolleibus1,Trolleibus2,Trolleibus3

urlpatterns = [
    path('',Trolleibus.as_view(), name='trolleibus'),
    path('1/',Trolleibus1.as_view(), name='trolleibus_1'),
    path('2/', Trolleibus2.as_view(), name='trolleibus_2'),
    path('3/',Trolleibus3.as_view(), name='trolleibus_3'),
]