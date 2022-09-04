from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='news_list'),
    path('advertisement/', views.Advertisements.as_view(), name='advertisement_list'),
    path('сontacts/', views.My_contacts.as_view(), name='contact_list'),
    path('about/', views.About_google.as_view(), name='About'),
]