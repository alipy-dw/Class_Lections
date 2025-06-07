from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import RegisterUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]