from django.shortcuts import render
from django.http import HttpResponse
from .models import list
# Create your views here.

def index(request):
    latest_items = list.objects.order_by('-pub_date')[:5]
    
    return HttpResponse("Seu Corno")

def info(request, list_id):
    response = "Vc está na info da tarefa %s."
    return HttpResponse(response % list_id)
