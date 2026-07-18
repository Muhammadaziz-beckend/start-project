# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

# from rest_framework.views import APIView
# from rest_framework.filters import (
#     SearchFilter,
#     OrderingFilter,
# )
# from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

# from apps.account.serializers import AuthTokenSerializer  # phone login
from rest_framework.authtoken.serializers import AuthTokenSerializer # username login
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *



class Login(GenericAPIView):
    serializer_class = AuthTokenSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                # "role": user.role,
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
