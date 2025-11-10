# api/docs.py
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path, include

# Swagger только для v1
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Client API",
        default_version='v1',
        description="Документация только для клиентов (v1)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path("api/v1/", include("api.v1.urls")),
    ],
)

# # Swagger только для Mbank
# schema_view_mbank = get_schema_view(
#     openapi.Info(
#         title="Mbank API",
#         default_version='v1',
#         description="Документация Mbank интеграции",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     patterns=[
#         path("api/mbank/", include("api.pay.urls")),
#     ],
# )
