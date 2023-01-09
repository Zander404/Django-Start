from collections import UserString
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class UserForm(UserCreationForm):
    mobile = forms.CharField(max_length=15, min_length=10)
    email = forms.EmailField(required=True)
    class Meta:
        models = User
        fields = ['username','password', 'fistname','email', 'mobile' ]
