from django.urls import include, path

from .views import (RegisterAPIView, 
                    LoginAPIView, 
                    UserAPIView, 
                    RefreshAPIView, 
                    LogoutAPIView,
                    ForgotAPIView,
                    ResetAPIView)

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', UserAPIView.as_view(), name='user'),
    path('refresh', RefreshAPIView.as_view(), name='refresh'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('forgot', ForgotAPIView.as_view(), name='forgot'),
    path('reset', ResetAPIView.as_view(), name='reset'),
]
