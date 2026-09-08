from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings

from apps.account.views.auth import Login

router = DefaultRouter()

urlpatterns = [
   
    #
    path("", include(router.urls)),
]


if settings.AUTH_MODE in ("jwt", "both"):
    urlpatterns += [
        path("auth/jwt/login/", TokenObtainPairView.as_view()),
        path("auth/jwt/refresh/", TokenRefreshView.as_view()),
    ]

if settings.AUTH_MODE in ("token", "both"):
    urlpatterns += [ path("auth/login/", Login.as_view(), name="login"),]