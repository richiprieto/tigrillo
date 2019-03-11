from django.db import models
from django.utils import timezone
# Create your models here.

class Match(models.Model):
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)

class Data(models.Model):

    escuela = models.CharField(max_length=200, blank=False)

    choices = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    sexo = models.CharField(max_length=1, choices=choices, default='F')
    edad = models.IntegerField()
    choices1 = (
            ('U', 'Urbano'),
            ('R', 'Rural'),
    )
    direccion = models.CharField(max_length=1, choices=choices1, default="U")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Sexo: {0} Direccion: {1}'.format(self.sexo, self.direccion)

class DataSet(Data):
    pass
