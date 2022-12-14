from django.shortcuts import render
from parsed_data.models import BlogData
from django.views.generic import *
# Create your views here.
class BlogDataLV(ListView):
    model= BlogData
    template_name = 'parsed_data/BlogData.html'

class BlogDataDV(DetailView):
    model= BlogData


    def home(request):
        class_object = BlogData.objects.all()
        return render(request, 'BlogData.html', {'class_object': class_object})   


