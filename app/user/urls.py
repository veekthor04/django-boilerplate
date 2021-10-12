from django.urls import path

from drf_yasg.utils import swagger_auto_schema

from .views import MyTokenObtainPairView, CreateUserView, \
    ProfileUserView, MyTokenRefreshView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('token/refresh/',
        MyTokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
