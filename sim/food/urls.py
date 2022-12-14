from django.urls import path 
from food import views

app_name = 'food'
urlpatterns = [
    # Example: /food/  
    path('', views.zipLV.as_view(), name='index'),
    path('zip/', views.zipLV.as_view(), name='zip_list'),

    path('zip/<int:pk>/', views.zipDV.as_view(), name='zip_detail'),
    path('zip/add/',views.zipCV.as_view(), name='zip_add'),
    path('zip/change/', views.zipChangeLV.as_view(), name='zip_change'),
    path('zip/<int:pk>/update/', views.zipUV.as_view(), name='zip_update'),
    path('zip/<int:pk>/delete/', views.zipDelV.as_view(), name='zip_delete'),

    
    path('food/<int:pk>/', views.foodDV.as_view(), name='food_detail'),
    path('food/add/', views.foodCV.as_view(), name='food_add'), 
    path('food/change/', views.foodChangeLV.as_view(), name='food_change'), 
    path('food/<int:pk>/update/' , views.foodUV.as_view(), name='food_update'), 
    path ('food/<int:pk>/delete/', views.foodDelV.as_view(), name='food_delete'),

]