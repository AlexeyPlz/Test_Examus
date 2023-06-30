from django.db import models


class Base(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, db_index=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, db_index=True)

    class Meta:
        abstract = True
