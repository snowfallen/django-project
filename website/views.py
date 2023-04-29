from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Menu


# Create your views here.
class Index(generic.TemplateView):
    template_name = 'website/index.html'


