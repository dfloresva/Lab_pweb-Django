from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    travell = Destination.objects.all()
    return render(request,"index.html",{'travell': travell})

def about(request):
    return render(request,"about.html",{})

def contact(request):
    return render(request,"contact.html",{})
