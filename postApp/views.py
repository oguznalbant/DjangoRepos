from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from postApp.external import *
# Create your views here.

@csrf_exempt
def home_view(request):
    return render(request,'home.html')

def planogram_view(request):
    return render(request,'planogram.html')

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
      data = request.body
      oguzhan()
       #  python methodu çağrılıp işlemler yapılacak

      return HttpResponse(data)