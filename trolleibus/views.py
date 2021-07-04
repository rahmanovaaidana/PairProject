from django.shortcuts import render
from django.views.generic import View



class Trolleibus(View):
    def get(self,request):
        return render(request,template_name='trolleibus/trolleibus.html')
 
class Trolleibus1(View):
    def get(self,request):
        return render(request,template_name='trolleibus/Trolleibus1.html')
    
class Trolleibus2(View):
    def get(self,request):
        return render(request,template_name='trolleibus/Trolleibus2.html')

class Trolleibus3(View):
    def get(self,request):
        return render(request,template_name='trolleibus/Trolleibus3.html')

