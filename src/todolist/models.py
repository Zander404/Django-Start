from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
import datetime
# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField("datepublished")
    note = models.TextField(max_length=450, blank=True, null=True)
    
    @admin.display(
        boolean=True,
        ordering='created',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now
 
    def __str__(self):
        return self.name

class toDo(models.Model):  
    master = models.ForeignKey(List, on_delete=models.CASCADE, default=0) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField('datepublished')


    def __str__(self):
        return str(self.id) 
