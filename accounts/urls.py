from django.urls import path
from .views import (
  HomeView, UserRegisterView, UserLoginView, UserLogoutView
)

app_name = 'accounts'

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('register/', UserRegisterView.as_view(), name='register'),
  path('login/', UserLoginView.as_view(), name='login'),
  path('logout/', UserLogoutView.as_view(), name='logout'),
]