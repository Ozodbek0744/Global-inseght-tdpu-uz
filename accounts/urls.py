from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, update_account_view, user_logout
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'


urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', registration_view),
    path('update', update_account_view),
    path('logout', user_logout)
]


