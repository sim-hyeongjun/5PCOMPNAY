
import requests
from bs4 import BeautifulSoup
from django.views.generic import *
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        url = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?page=1&perPage=10&cond%5BSUBSCRPT_AREA_CODE_NM%3A%3AEQ%5D=%EC%84%9C%EC%9A%B8&cond%5BRCRIT_PBLANC_DE%3A%3AGTE%5D=2022-11-01'
        params = {'serviceKey':'LU10B4YcmjsCI3uZN3q0+dsSE60qU7AnQEZUHv2rYjsA7VkxxjWC1lELnvBA6EHcGY4o4fF2i9lNKbCHmuNZZA=='
         }
        response = requests.get(url,params=params)
        import json

        context = super().get_context_data(**kwargs)
        context["result"] = json.loads(response.text)
        return context
