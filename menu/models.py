from django.db import models

class Administrador(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'Administrador'

class Usuarios(models.Model):
    name = models.CharField(max_length=255)
    ip = models.PositiveIntegerField(primary_key=True)
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Usuarios'

class Portas(models.Model):
    ip = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ip')
    port = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Portas'
        unique_together = (('ip', 'port'),)


class Responsibles(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.PositiveIntegerField()
    what = models.CharField(max_length=255)
    added = models.DateTimeField()
    action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Responsibles'
        unique_together = (('id', 'what', 'ip', 'action', 'added'),)