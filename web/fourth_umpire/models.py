from django.db import models
from django.utils import timezone

from import_export import resources
# Create your models here.

class DataMatch(models.Model):
    eleccion_carrera = (
        ('1',	'Ing. Electrónica'),
        ('2',	'Med. Veterinaria'),
        ('3',	'Ing. Eléctrica'),
        ('4',	'Ing. Sistemas'),
        ('5',	'Ing. Mecatrónica'),
    )
    carrera = models.CharField(max_length=1, choices=eleccion_carrera, default='1')
    eleccion_ciclo = (
        ('1',	'1er Ciclo'),
        ('2',	'2do Ciclo'),
        ('3',	'3er Ciclo'),
        ('4',	'4to Ciclo'),
        ('5',	'5to Ciclo'),
        ('6',	'6to Ciclo'),
        ('7',	'7mo Ciclo'),
        ('8',	'8vo Ciclo'),
        ('9',	'9no Ciclo'),
        ('10', '10mo Ciclo'),
    )
    ciclo = models.CharField(max_length=1, choices=eleccion_ciclo, default='1')
    eleccion_sede = (
        ('1'	, 'Cuenca'),
        ('2'	, 'Quito'),
        ('3'	, 'Guayaquil'),
    )
    sede = models.CharField(max_length=1, choices=eleccion_sede, default='1')

    document = models.FileField(upload_to='documents/', blank=False, null=True)

#    class Meta:
#        abstract = True

class Match(DataMatch):
    pass

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

class PersonResource(resources.ModelResource):
    class Meta:
        model = DataSet
