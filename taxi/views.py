from django.shortcuts import render
from django.views.generic import View



class Taxi(View):
    def get(self,request):
        return render(request,template_name='taxi/taxi.html')

class Taxi1(View):
    def get(self,request):
        return render(request,template_name='taxi/taxi1.html')


class Taxi2(View):
    def get(self,request):
        return render(request,template_name='taxi/taxi2.html')

class Taxi3(View):
    def get(self,request):
        return render(request,template_name='taxi/taxi3.html')
    


