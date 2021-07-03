from django.shortcuts import render

from django.views.generic import View

class Marshrutka_1View(View):
    def get(self, request):
        return render(request, template_name='marshrutka/marshrutka_1.html')

class Marshrutka_2View(View):
    def get(self, request):
        return render(request, template_name='marshrutka/marshrutka_2.html')

class Marshrutka_3View(View):
    def get(self, request):
        return render(request, template_name='marshrutka/marshrutka_3.html')

class MarshrutkiView(View):
    def get(self, request):
        return render(request, template_name='marshrutka/marshrutki.html')