from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Menu


# Create your views here.
def index(request):
    menu_item = Menu
    context = {
        'menu_item': menu_item
    }
    return render(request, 'website/index.html', context)

