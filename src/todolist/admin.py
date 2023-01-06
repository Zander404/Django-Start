from django.contrib import admin
from .models import *

# Register your models here.

class toDo(admin.TabularInline):
    model = toDo
    extra = 1

class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        ("Publicacao", {'fields': ['created']}),
        ("Descrição", {'fields': ['note']}),
        
    ]
    inlines =[toDo]
    list_display = ('name', 'created')
    list_filter = ['created']
    search_fields = ['name'] 

admin.site.register(List, ListAdmin)