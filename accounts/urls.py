from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserApiView.as_view()),
    path('users_list/', views.UserListApiView.as_view()),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls
