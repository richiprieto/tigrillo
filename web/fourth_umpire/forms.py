from django import forms
from .models import Match

eleccion_carrera = (
    (1,	'Ing. Electrónica'),
    (2,	'Med. Veterinaria'),
    (3,	'Ing. Eléctrica'),
    (4,	'Ing. Sistemas'),
    (5,	'Ing. Mecatrónica'),
)

eleccion_ciclo = (
    (1,	'1er Ciclo'),
    (2,	'2do Ciclo'),
    (3,	'3er Ciclo'),
    (4,	'4to Ciclo'),
    (5,	'5to Ciclo'),
    (6,	'6to Ciclo'),
    (7,	'7mo Ciclo'),
    (8,	'8vo Ciclo'),
    (9,	'9no Ciclo'),
    (10, '10mo Ciclo'),

)

eleccion_sede = (
    (1	, 'Cuenca'),
    (2	, 'Quito'),
    (3	, 'Guayaquil'),
)

class PreMatch(forms.Form):
    team1 = forms.ChoiceField(choices=eleccion_carrera, widget=forms.Select())
    team2 = forms.ChoiceField(choices=eleccion_ciclo, widget=forms.Select())
    venue = forms.ChoiceField(choices=eleccion_sede, widget=forms.Select())
