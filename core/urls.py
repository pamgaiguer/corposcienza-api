from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,   # login -> access + refresh
    TokenRefreshView,      # refresh do access
    TokenVerifyView,       # (opcional) verificar token
)

# JWT Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),  # <— adiciona tela de login
    path('api/', include('apps.pacientes.urls')),

    # Gera o schema em JSON

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Endpoints JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # (opcional) “logout” invalidando o refresh token:
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # accounts
    path("api/accounts/", include("apps.accounts.urls")),  # <- AQUI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Interface Swagger usando o schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]
