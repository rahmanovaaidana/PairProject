from django.shortcuts import render

from django.views.generic import View

class Avtobus_1View(View):
    def get(self, request):
        return render(request, template_name='avtobus/avtobus_1.html')

class Avtobus_2View(View):
    def get(self, request):
        return render(request, template_name='avtobus/avtobus_2.html')

class Avtobus_3View(View):
    def get(self, request):
        return render(request, template_name='avtobus/avtobus_3.html')

class AvtobusyView(View):
    def get(self, request):
        return render(request, template_name='avtobus/avtobusy.html')




