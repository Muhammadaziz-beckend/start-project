import django
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework import serializers
from rest_framework import status

class SerializeByActionMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        if self.action == "partial_update" or self.action == "update_partial":
            serializer = self.serializer_classes.get("update", None)
        else:
            serializer = self.serializer_classes.get(self.action, None)
        return serializer if serializer is not None else super().get_serializer_class()


class PermissionByActionMixin:
    permission_classes_by_action = {}

    def get_permissions(self):
        permission_classes = self.permission_classes_by_action.get(self.action, None)
        if self.action == "partial_update" or self.action == "update_partial":
            permission_classes = self.permission_classes_by_action.get("update", None)
        if permission_classes is None:
            return super().get_permissions()
        return [permission() for permission in permission_classes]


class MultipleDestroyMixinSerializer(serializers.Serializer):
    ids = serializers.ListSerializer(child=serializers.CharField())


class MultipleDestroyMixin:
    multiple_delete_permission = permission_classes

    @permission_classes([multiple_delete_permission])
    @action(methods=["POST"], url_path="multiple-delete", detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        queryset = self.get_queryset()
        items = queryset.filter(pk__in=serializer.data["ids"])
        not_deleted_items = []
        for item in items:
            item_id = item.pk
            try:
                item.delete()
            except django.db.models.deletion.ProtectedError as e:
                not_deleted_items.append(item_id)
        return Response(
            {"not_deleted_items": not_deleted_items},
            status=(
                status.HTTP_204_NO_CONTENT
                if len(not_deleted_items) == 0
                else status.HTTP_423_LOCKED
            ),
        )

    def get_serializer_class(self):
        path = self.request.path.split("/")[-2]
        if path == "multiple-delete":
            return MultipleDestroyMixinSerializer
        return super().get_serializer_class()


class UltraModelViewSet(
    PermissionByActionMixin,
    SerializeByActionMixin,
    ModelViewSet,
): ...
