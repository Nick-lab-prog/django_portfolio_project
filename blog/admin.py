from django.contrib import admin
from .models import Blog #importing the blog class from the module

# Register your models here.
#qui vengono mostrati i models 

admin.site.register(Blog)