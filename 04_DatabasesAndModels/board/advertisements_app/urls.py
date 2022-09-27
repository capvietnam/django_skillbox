from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('advertisement/', HomeAdvertisement.as_view(), name='advertisements-list'),
    path('advertisement/<int:pk>/', Advertisement.as_view(), name='advertisement-detail')
]
