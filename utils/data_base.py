from asgiref.sync import sync_to_async

# from apps.tasks.models import Task

# @sync_to_async
# def get_order(id):
#     """Проверка если пользователь в базе"""
#     try:
#         return Task.objects.get(pk=id)
#     except Task.DoesNotExist:
#         return None