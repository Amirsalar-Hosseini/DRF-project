from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-token-auth/', drf_views.obtain_auth_token),
]