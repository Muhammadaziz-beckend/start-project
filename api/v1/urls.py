from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.account.views.auth import Login

router = DefaultRouter()

urlpatterns = [
    path("auth/login/", Login.as_view(), name="login"),
    #
    path("", include(router.urls)),
]
