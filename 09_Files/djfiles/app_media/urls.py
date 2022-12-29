from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path(r'upload_file/', UploadFile, name=r'upload-file'),
    # path(r'upload_avatar/', UploadAvatar, name=r'upload-avatar'),
    path(r'upload_files/', UploadFiles, name=r'upload-files'),
]
