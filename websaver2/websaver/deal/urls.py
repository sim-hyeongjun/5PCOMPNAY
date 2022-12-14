from deal import views
from django.urls import path

app_name = 'deal'

urlpatterns = [
    path('', views.DealView.as_view(), name='index'),

]