from django.urls import path
from . import views
from .views import (CustomTokenObtainPairView, UserProfileView, UserRegisterView,)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home, name="home"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
# Rotas da API (para o aplicativo mobile)
    path('api/register/', UserRegisterView.as_view(), name='api_register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='api_token_obtain_pair'),
    path('api/profile/', UserProfileView.as_view(), name='api_profile'),
]