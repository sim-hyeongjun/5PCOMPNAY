from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import *
from poll.models import News
from django.conf import settings
from poll.forms import NewsSearchForm
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.db.models import Q
from django.shortcuts import render
from tkinter.messagebox import RETRY
from django.views.generic.dates import *

'''

class PollLV(ListView):
    model = poll
    template_name = 'poll/poll.html'
    context_object_name = 'polls'
class pollDV(DetailView):
    model = poll
    fields = ['title','link','img']
    success_url = reverse_lazy('bookmark:index')
'''



# Create your views here.
class NewsLV(ListView):
    model = News
    template_name = 'poll/News_all.html'
    context_object_name = 'News'
    paginate_by = 5
  

class NewsDV(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['disqus_short']= f'{settings.DISQUS_SHORTNAME}'
        context['disqus_id']= f"News-{self.object.id}-{self.object.slug}"
        context['disqus_url']= f'{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}'
        context['disqus_title'] = f'{self.object.slug}'
        return context


class NewsAV(ArchiveIndexView):
    model = News
    date_field = 'modify_dt'


class NewsYAV(YearArchiveView):
    model = News
    date_field = 'modify_dt'
    make_object_list = True
    # month_format = '%d' # 디폴트 값


class NewsMAV(MonthArchiveView):
    model = News
    date_field = 'modify_dt'
    #month_format = '%m'


class NewsDAV(DayArchiveView):
    model = News
    date_field = 'modify_dt'
    #month_format = '%m'


class NewsTAV(TodayArchiveView):
    model = News
    date_field = 'modify_dt'


class TagCloudTV(TemplateView):
    template_name='taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    model=News 
    template_name = 'taggit/taggit_News_list.html'

    def get_queryset(self):
        return News.objects.filter( tags__name = self.kwargs.get('tags'))
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] =self.kwargs['tag']
        return context 


class SearchFV(FormView):
    form_class = NewsSearchForm
    template_name='poll/News_search.html'
    
    def form_valid(self,form):
        searchWord =form.cleaned_data['search_word']
        News_list = News.objects.filter(Q(title__icontains =searchWord)|
                                        Q(description__icontains =searchWord)|
                                        Q(content__icontains =searchWord)).distinct()  
        context = {'form' : form,
                    'search_term': searchWord,
                    'object_list':News_list 
                    }
        return render(self.request, self.template_name, context)

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'slug','description', 'content','tags']
    initial={'slug' : '자동으로-완성되니-적지마시오'}
    success_url = reverse_lazy('poll:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NewsChangeLV(LoginRequiredMixin, ListView):
    template_name = 'poll/News_change_list.html'

    def get_queryset(self):
        return News.objects.filter(owner = self.request.user)


class NewsUpdateView(OwnerOnlyMixin, UpdateView):
    model =News
    fields = ['title', 'slug','description', 'content','tags']
    success_url = reverse_lazy('poll:index')


#작성자만 삭제 할수 있도록
class NewsDeleteView(OwnerOnlyMixin, DeleteView):
    model =News
    
    success_url = reverse_lazy('poll:index')
