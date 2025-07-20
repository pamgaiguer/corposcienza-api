from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Corpo Scienza",
      default_version='v1',
      description="Documentação da Corpo Scienza",
      contact=openapi.Contact(email="pamella@gaiguer.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Gera o schema em JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Interface Swagger usando o schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include('apps.pacientes.urls')),  # ou sua app
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
