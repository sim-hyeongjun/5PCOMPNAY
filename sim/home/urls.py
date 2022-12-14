from django.urls import path 
from home import views

app_name = 'home'
urlpatterns = [
    # Example: /home/  
    path('', views.townLV.as_view(), name='index'),
    path('town/', views.townLV.as_view(), name='town_list'),

    path('town/<int:pk>/', views.townDV.as_view(), name='town_detail'),
    path('town/add/',views.townCV.as_view(), name='town_add'),
    path('town/change/', views.townChangeLV.as_view(), name='town_change'),
    path('town/<int:pk>/update/', views.townUV.as_view(), name='town_update'),
    path('town/<int:pk>/delete/', views.townDelV.as_view(), name='town_delete'),

    
    path('home/<int:pk>/', views.homeDV.as_view(), name='home_detail'),
    path('home/add/', views.homeCV.as_view(), name='home_add'), 
    path('home/change/', views.homeChangeLV.as_view(), name='home_change'), 
    path('home/<int:pk>/update/' , views.homeUV.as_view(), name='home_update'), 
    path ('home/<int:pk>/delete/', views.homeDelV.as_view(), name='home_delete'),

]