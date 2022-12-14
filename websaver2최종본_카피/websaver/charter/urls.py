from charter import views
from django.urls import path

app_name = 'charter'

urlpatterns = [
    path('', views.charter.as_view(), name='index'),

]