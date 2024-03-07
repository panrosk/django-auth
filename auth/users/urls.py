from .views import ListCreateUser,ListUser,DetailUser
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
 
app_name = "users"


urlpatterns = [
        path('register', ListCreateUser.as_view(), name="register"),
        path('login', TokenObtainPairView.as_view(), name="login"),
        path('refresh', TokenRefreshView.as_view(), name="refresh"),
        path('users', ListUser.as_view(), name="users"),
        path('detail', DetailUser.as_view(), name="detail"),
]



