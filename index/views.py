from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from .models import Series

def index(request):
    return render(request,'index.html')




class Seri(TemplateView):


    def get(self,request):

        series=Series.objects.all()
        return render(request,'series.html',{'series':series})




