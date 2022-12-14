from parsed_data import views
from django.urls import path

app_name = 'parsed_data'

urlpatterns = [
    path('', views.BlogDataLV.as_view(), name='index'),
    path('parsed_data', views.BlogDataLV.as_view(), name='parsed_data_list'),
    path('parsed_data/<int:pk>/', views.BlogDataDV.as_view(), name='parsed_data_detail'),

]