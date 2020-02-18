from django.db import models

class Administrador(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Administrador'

class Usuarios(models.Model):
    name = models.CharField(max_length=255)
    ip = models.PositiveIntegerField(primary_key=True)
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Usuarios'

class Portas(models.Model):
    ip = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ip')
    port = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Portas'


class Responsibles(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.PositiveIntegerField()
    what = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)
    class Meta:
        db_table = 'Responsibles'