from django.urls import path, include
from api.docs import schema_view_v1

urlpatterns = [
    # Твои основные эндпоинты
    # path("orders/", include("api.orders.urls")),

    # Swagger для v1
    path("swagger/", schema_view_v1.with_ui('swagger', cache_timeout=0), name='swagger-v1'),
    path("redoc/", schema_view_v1.with_ui('redoc', cache_timeout=0), name='redoc-v1'),
]
