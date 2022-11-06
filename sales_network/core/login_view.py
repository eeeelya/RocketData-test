from rest_framework.response import Response
from rest_framework import views, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from django.contrib.auth import authenticate

from sales_network import settings
from core.login_serializer import LoginSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()
        response = Response()

        user = authenticate(username=serializer.data["username"], password=serializer.data["password"])
        if user is not None:
            data = get_tokens_for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            )
            csrf.get_token(request)
            response.data = {"Success": "Login successfully", "data": data}

            return response
        else:
            return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
