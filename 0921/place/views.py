from django.shortcuts import render
from django.views.generic import *
from .models import File, Place
# Create your views here.

class FileLV(ListView):
    model = File
    
class FileDV(DetailView):
    model = File

class PlaceDV(DetailView):
    model = Place