from django.shortcuts import render
from deal.models import deal
from django.views.generic import *
# Create your views here.
class DealView(TemplateView):
    template_name = 'deal/deal.html'

