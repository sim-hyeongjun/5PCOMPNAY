import code
from multiprocessing import context
from pipes import Template
from pydoc import describe
from re import template

from tkinter.messagebox import RETRY
from tkinter.tix import Form
from django.shortcuts import render
from django.views.generic.dates import *
from airport.models import airport
from django.conf import settings

from django.db.models import Q
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
import requests
#

# Create your views here.
class airportall(TemplateView):
    model= airport
    template_name = 'airport/airport_all.html'

class airport1(TemplateView):
    
    template_name = 'airport/airport_1.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKJB', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport2(TemplateView):
    
    template_name = 'airport/airport_2.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKJJ', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport3(TemplateView):
    
    template_name = 'airport/airport_3.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKJK', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport4(TemplateView):
    
    template_name = 'airport/airport_4.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKJY', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport5(TemplateView):
    
    template_name = 'airport/airport_5.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKNW', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context

class airport6(TemplateView):
    
    template_name = 'airport/airport_6.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKNW', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport7(TemplateView):
    
    template_name = 'airport/airport_7.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKNY', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport8(TemplateView):
    
    template_name = 'airport/airport_8.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKPK', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport9(TemplateView):
    
    template_name = 'airport/airport_9.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKPS', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport10(TemplateView):
    
    template_name = 'airport/airport_10.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKPU', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport11(TemplateView):
    
    template_name = 'airport/airport_11.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKSI', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport12(TemplateView):
    
    template_name = 'airport/airport_12.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKSS', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport13(TemplateView):
    
    template_name = 'airport/airport_13.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKTH', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport14(TemplateView):
    
    template_name = 'airport/airport_14.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKTN', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
class airport15(TemplateView):
    
    template_name = 'airport/airport_15.html'
    def get_context_data(self, **kwargs):
        key='AAAS9ZmuHQ8ul8jOsCMUTd+VwHzoVIN/qa2GAqr78TcKiqTOkAGt/TV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw=='
        url = 'http://apis.data.go.kr/1613000/DmstcFlightNvgInfoService/getFlightOpratInfoList'

 

        params ={'serviceKey' : key,  'numOfRows' : 50, '_type' : 'json', 'depAirportId' : 'NAARKPC', 'arrAirportId' : 'NAARKTU', 'depPlandTime' : '20221001'}

        #params ={'serviceKey' : 'AAAS9ZmuHQ8ul8jOsCMUTd%2BVwHzoVIN%2Fqa2GAqr78TcKiqTOkAGt%2FTV1oYBIXNf8KrxonohWhHhk7AYt4gFTdw%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'json', 'depAirportId' : 'NAARKJJ', 'arrAirportId' : 'NAARKPC', 'depPlandTime' : '20201201', 'airlineId' : 'AAR' }

        response = requests.get(url, params=params)
        import json
        
        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context

