from django.urls import path 
from . import views
from . import models

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:list_id>/", views.detail, name="detail")
]