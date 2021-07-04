from django.urls import path
from .views import Marshrutka_1View, Marshrutka_2View, Marshrutka_3View, MarshrutkiView

urlpatterns = [
    path('1/', Marshrutka_1View.as_view(), name='marshrutka_1'),
    path('2/', Marshrutka_2View.as_view(), name='marshrutka_2'),
    path('3/', Marshrutka_3View.as_view(), name='marshrutka_3'),
    path('', MarshrutkiView.as_view(), name='marshrutki'),
    
    
]