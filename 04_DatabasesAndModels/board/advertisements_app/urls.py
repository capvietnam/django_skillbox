from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('advertisement/', Advertisement.as_view(), name='advertisements-list'),
    path('advertisement/<int:pk>/', Get_advertisement.as_view(), name='advertisement-detail')
]
