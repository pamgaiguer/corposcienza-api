from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .serializers import LoginSerializer, TokenPairSerializer, LogoutSerializer

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="accounts_login",
        request=LoginSerializer,
        responses={200: TokenPairSerializer},
        examples=[
            OpenApiExample(
                "Login exemplo",
                value={"username": "admin", "password": "sua_senha"},
                request_only=True,
            )
        ],
        tags=["api"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LogoutView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="accounts_logout",
        request=LogoutSerializer,
        responses={200: None},
        examples=[OpenApiExample("Logout exemplo", value={"refresh": "REFRESH_JWT"})],
        tags=["api"],
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = RefreshToken(serializer.validated_data["refresh"])
            token.blacklist()  # invalida o refresh
        except TokenError:
            # já inválido/expirado — responde OK mesmo assim
            pass
        return Response(status=status.HTTP_200_OK)
