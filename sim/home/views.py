
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings

from .models import town, home
from .forms import homeInlineFormSet
from mysite.views import OwnerOnlyMixin




# Create your views here.
class townLV(ListView):
    model = town
    
class townDV(DetailView):
    model = town

class homeDV(DetailView):
    model = home

    
class townCV(LoginRequiredMixin, CreateView):
    model=town
    fields = ('name', 'description')
    success_url = reverse_lazy('home:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = homeInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = homeInlineFormSet()
        return context
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for homeform in formset:
            homeform.instance.owner = self.request.user
        if formset.is_valid() :
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class townChangeLV(LoginRequiredMixin, ListView):
    template_name = 'home/town_change_list.html'
    
    def get_queryset(self):
        return town.objects.filter(owner = self.request.user)
    
class townUV(OwnerOnlyMixin, UpdateView):
    model = town
    fields = ('name', 'description')
    success_url = reverse_lazy('home:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = homeInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else :
            context['formset'] = homeInlineFormSet(instance=self.object)
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
        
class townDelV(OwnerOnlyMixin, DeleteView):
    model = town
    success_url = reverse_lazy('home:index')

class homeCV(LoginRequiredMixin, CreateView):
    model = home
    fields = ('town', 'title', 'image', 'description')
    success_url = reverse_lazy('home:index')
    
    def form_valid(self, form) :
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class homeChangeLV(LoginRequiredMixin, ListView):
    template_name = 'home/home_change_list.html'
    
    def get_queryset(self):
        return home.objects.filter(owner=self.request.user)
    
class homeUV(OwnerOnlyMixin, UpdateView):
    model = home
    fields = ('town', 'title', 'image', 'description')
    success_url = reverse_lazy('home:index')
    
class homeDelV(OwnerOnlyMixin, DeleteView):
    model = home
    success_url = reverse_lazy('home:index')

class homeLV(ListView):
    model = home
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

class homeDV(DetailView):
    model = home

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['disqus_short']= f'{settings.DISQUS_SHORTNAME}'
        context['disqus_id']= f"post-{self.object.id}-{self.object.title}"
        context['disqus_url']= f'{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}'
        context['disqus_title'] = f'{self.object.title}'
        return context
