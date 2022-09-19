from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('advertisement/', views.Advertisement.as_view(), name='advertisements-list'),
    path('advertisement/<int:id>/', views.get_advertisement.as_view(), name='advertisement')
]
