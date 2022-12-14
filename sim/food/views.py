
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings

from .models import zip, food
from .forms import foodInlineFormSet
from mysite.views import OwnerOnlyMixin

# Create your views here.
class zipLV(ListView):
    model = zip
    
class zipDV(DetailView):
    model = zip

class foodDV(DetailView):
    model = food

    
class zipCV(LoginRequiredMixin, CreateView):
    model=zip
    fields = ('name', 'description')
    success_url = reverse_lazy('food:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = foodInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = foodInlineFormSet()
        return context
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for foodform in formset:
            foodform.instance.owner = self.request.user
        if formset.is_valid() :
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class zipChangeLV(LoginRequiredMixin, ListView):
    template_name = 'food/zip_change_list.html'
    
    def get_queryset(self):
        return zip.objects.filter(owner = self.request.user)
    
class zipUV(OwnerOnlyMixin, UpdateView):
    model = zip
    fields = ('name', 'description')
    success_url = reverse_lazy('food:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = foodInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else :
            context['formset'] = foodInlineFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else :
            return self.render_to_response(self.get_context_data(form=form))
        
class zipDelV(OwnerOnlyMixin, DeleteView):
    model = zip
    success_url = reverse_lazy('food:index')

class foodCV(LoginRequiredMixin, CreateView):
    model = food
    fields = ('zip', 'title', 'image', 'description')
    success_url = reverse_lazy('food:index')
    
    def form_valid(self, form) :
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class foodChangeLV(LoginRequiredMixin, ListView):
    template_name = 'food/food_change_list.html'
    
    def get_queryset(self):
        return food.objects.filter(owner=self.request.user)
    
class foodUV(OwnerOnlyMixin, UpdateView):
    model = food
    fields = ('zip', 'title', 'image', 'description')
    success_url = reverse_lazy('food:index')
    
class foodDelV(OwnerOnlyMixin, DeleteView):
    model = food
    success_url = reverse_lazy('food:index')

class foodLV(ListView):
    model = food
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

class foodDV(DetailView):
    model = food

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['disqus_short']= f'{settings.DISQUS_SHORTNAME}'
        context['disqus_id']= f"post-{self.object.id}-{self.object.title}"
        context['disqus_url']= f'{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}'
        context['disqus_title'] = f'{self.object.title}'
        return context