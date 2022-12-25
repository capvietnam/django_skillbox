from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'login/', UserLoginView.as_view(), name=r'user-login'),
    path(r'register/', UserRegisterView, name=r'user-register'),
    path(r'logout/', UserLogoutView.as_view(), name=r'user-logout'),
    path(r'profile/', views.profile, name=r'user-profile'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
