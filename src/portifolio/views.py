from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from portifolio.models import UserForm
 
# Create your views here.

def UserCreate(request):
    return render(request, 'portifolio/dashboard.html')
