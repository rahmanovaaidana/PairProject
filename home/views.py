from django.shortcuts import render
from django.views.generic import View



class Home(View):
    def get(self,request):
        return render(request,template_name='home/home.html')
    
