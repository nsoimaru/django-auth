import re
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.authentication import create_access_token, JWTAuthentication

from core.models import User

from .serializer import UserSerializer

class RegisterAPIView(APIView):

    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match!')

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_access_token(user.id)

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }
        return response

class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        return Response(UserSerializer(request.user).data)