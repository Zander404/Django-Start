from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import List
# Create your views here.

def index(request):
    latest_items = List.objects.order_by('-created')
    context = {'latest_items': latest_items}
    return render(request,'todolist/index.html', context)

def detail(request, list_id):
    note = get_object_or_404(List, pk=list_id )
    return render(request, 'todolist/detail.html', {'note': note})
