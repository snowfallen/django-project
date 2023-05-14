from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template import loader
from .models import Post


# Create your views here.
def posts(request):
    post_list = get_object_or_404(Post)
    return render(request, "website/dashboard.html", {"posts": post_list})

