from django.shortcuts import render
from .models import Service
# Create your views here.

def services(request):
    services = Service.objects.all()#para recuperar todo de la base de datos
    return render(request,"services/services.html", {'services':services})#se envia en un diccionario