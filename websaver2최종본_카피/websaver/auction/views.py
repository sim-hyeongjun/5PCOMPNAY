from django.shortcuts import render
from deal.models import deal
from django.views.generic import *
# Create your views here.
class auction(TemplateView):
    template_name = 'auction/auction.html'