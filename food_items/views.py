from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageModel, Menu

# Create your views here.
def home(request):
    img = ImageModel.objects.all()
    menu = Menu.objects.all()
    context = {
        'img':img,
        'menu':menu,
    }
    return render(request, "home.html", context)