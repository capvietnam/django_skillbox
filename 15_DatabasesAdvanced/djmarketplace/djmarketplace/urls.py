from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Items API",
        default_version='v1',
        description='Описание проекта',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@company.local"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_goods.urls')),
    path('app_users/', include('app_users.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
