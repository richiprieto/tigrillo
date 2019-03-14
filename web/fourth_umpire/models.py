from django.db import models
from django.utils import timezone

# Create your models here.

class Match(models.Model):
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
