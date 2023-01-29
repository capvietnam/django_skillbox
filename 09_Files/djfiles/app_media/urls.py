from django.urls import path
from .views import *

urlpatterns = [
    path(r'upload_file/', UploadFile, name=r'upload-file'),
    # path(r'upload_avatar/', UploadAvatar, name=r'upload-avatar'),
    path(r'upload_files/', UploadFiles, name=r'upload-files'),
]
