from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views
from rest_framework import routers


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-token-auth/', drf_views.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls