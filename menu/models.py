from django.db import models
from datetime import datetime

class Usuarios(models.Model):
    name = models.CharField(max_length=255)
    ip = models.PositiveIntegerField(primary_key=True)
    date_add = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table = 'Usuarios'

class Portas(models.Model):
    ip = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ip')
    port = models.IntegerField()
    date_add = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table = 'Portas'


class Responsibles(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.PositiveIntegerField()
    what = models.CharField(max_length=255)
    added = models.DateTimeField(default=datetime.now)
    action = models.CharField(max_length=255)
    class Meta:
        db_table = 'Responsibles'