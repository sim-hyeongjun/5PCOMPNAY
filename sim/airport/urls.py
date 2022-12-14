from django.urls import path, re_path
from airport import views

app_name = 'airport'

urlpatterns = [
    path('', views.airportall.as_view(), name='index'),
    path('airport/', views.airportall.as_view(), name='airport_all'),
    


    path('airport/1/', views.airport1.as_view(), name='airport_1'),
    path('airport/2/', views.airport2.as_view(), name='airport_2'),
    path('airport/3/', views.airport3.as_view(), name='airport_3'),
    path('airport/4/', views.airport4.as_view(), name='airport_4'),
    path('airport/5/', views.airport5.as_view(), name='airport_5'),
    path('airport/6/' , views.airport6.as_view(),name='airport_6'),
    path('airport/7/',views.airport7.as_view(), name='airport_7'),    
    path('airport/8/',views.airport8.as_view(),name = 'airport_8'),
    path('airport/9/', views.airport9.as_view(),name='airport_9'),
    path('airport/10/', views.airport10.as_view(),name='airport_10'),
    path('airport/11/', views.airport11.as_view(),name='airport_11'),
    path('airport/12/', views.airport12.as_view(),name='airport_12'),
    path('airport/13/', views.airport13.as_view(),name='airport_13'),
    path('airport/14/', views.airport14.as_view(),name='airport_14'),
    path('airport/15/', views.airport15.as_view(),name='airport_15'),
]
