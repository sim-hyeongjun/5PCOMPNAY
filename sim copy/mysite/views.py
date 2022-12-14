from multiprocessing import context
from urllib import request, response
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
import requests

class HomeView(TemplateView):
    template_name = 'home.html'
    
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    Permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj =self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


        

class movieAPI(TemplateView):
    template_name = 'movie_page.html'

    def get_context_data(self, **kwargs):
        key='fc5bddbcf94d343459bad48d998d1611'
        date ='20220101'
        url ='http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}'.format(key,date)
        #키값이랑 원하는 날짜{}로 변경
        response =requests.get(url)
        r_date= response.json()
        
        context = super().get_context_data(**kwargs)
        context['boxOfficeResult']=r_date['boxOfficeResult']
        return context

class airAPI(TemplateView):
    template_name = 'air.html'

    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKSS', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        print(response.text)
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
