from django.urls import include, path

from .views import RegisterAPIView, LoginAPIView, UserAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', UserAPIView.as_view(), name='user'),
]
