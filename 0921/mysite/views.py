import imp
from sre_constants import SUCCESS
from django.views.generic import *
from blog.models import Post 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name='registration/register.html'
    template_name = UserCreationForm 
    success_url= reverse_lazy('register_done') 

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
