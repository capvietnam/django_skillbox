from django.urls import path
from .views import *

urlpatterns = [
    path(r'upload_file/', UploadFile, name=r'upload-file'),
]
