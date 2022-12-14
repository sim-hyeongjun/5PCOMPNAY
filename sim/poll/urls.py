from django.urls import path, re_path

from poll import views

'''
app_name = News'
urlpatterns = [
    path('', views.PollLV.as_view(), name='index'),
    path(News/', views.PollLV.as_view(), name=News_list'),
    
]
'''
app_name = 'poll'
urlpatterns = [
    path('', views.NewsLV.as_view(), name='index'),
    path('News/', views.NewsLV.as_view(), name='News_list'),
    
    re_path(r'^News/(?P<slug>[-\w]+)/$', views.NewsDV.as_view(), name='News_detail'),

    path('archive/', views.NewsAV.as_view(), name='News_archive'),
    path('archive/<int:year>/', views.NewsYAV.as_view(), name='News_year_archive'),
    path('archive/<int:year>/<str:month>/', views.NewsMAV.as_view(), name='News_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>', views.NewsDAV.as_view(), name='News_day_archive'),
    path('archive/today/', views.NewsTAV.as_view(), name='News_today_archive'),
    path('tag/' , views.TagCloudTV.as_view(),name='tag_cloud'),
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(), name='tagged_object_list'),    
    path('search/',views.SearchFV.as_view(),name = 'search'),
    path('add/', views.NewsCreateView.as_view(),name='add'),
    path('change/', views.NewsChangeLV.as_view(),name='change'),
    path('<int:pk>/update/', views.NewsUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(),name='delete'),
]
