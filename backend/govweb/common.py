from django.db.models import Q, F, FloatField
from django.db.models.functions import Cast, Concat
from django.db.models.fields import DateField, CharField
from django.db.models import Value
from django.db import models 


class BigAutoField(models.fields.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.__class__.__module__:
            return 'bigint AUTO_INCREMENT'
        return super(BigAutoField, self).db_type(connection)
