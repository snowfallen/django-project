from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard')
]
