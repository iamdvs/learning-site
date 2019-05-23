from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return render(request,'index.html')




class Series(TemplateView):


    def get(self,request):
        return render(request,'series.html')




