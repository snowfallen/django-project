from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Post


# Create your views here.
class Dashboard(generic.TemplateView):
    template_name = 'website/dashboard.html'


