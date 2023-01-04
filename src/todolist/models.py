from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class toDo(models.Model):   
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField('datepublished')

    def __str__(self):
        return str(self.id) 

class list(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField("datepublished")
    note = models.TextField(max_length=450, blank=True, null=True)

    def __str__(self):
        return self.name