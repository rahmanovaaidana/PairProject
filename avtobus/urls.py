from django.urls import path
from .views import Avtobus_1View, Avtobus_2View, Avtobus_3View, AvtobusyView

urlpatterns = [
    path('1/', Avtobus_1View.as_view(), name='avtobus_1'),
    path('2/', Avtobus_2View.as_view(), name='avtobus_2'),
    path('3/', Avtobus_3View.as_view(), name='avtobus_3'),
    path('', AvtobusyView.as_view(), name='avtobusy'),
    
    
]