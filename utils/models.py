from django.db import models


class DataTimeCUAbstract(models.Model):
    create_dt = models.DateTimeField("Дата создания",auto_now_add=True)
    update_dt = models.DateTimeField("Дата обновления",auto_now=True)

    class Meta:
        abstract = True