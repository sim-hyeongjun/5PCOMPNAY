from auction import views
from django.urls import path

app_name = 'auction'

urlpatterns = [
    path('', views.auction.as_view(), name='index'),

]