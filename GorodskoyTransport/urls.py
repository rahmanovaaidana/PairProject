from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taxi/', include('taxi.urls')),
    path('trolleibus/', include('trolleibus.urls')),
    path('home/', include('home.urls')),

]

