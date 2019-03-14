from django import forms
#from .models import Match
from .models import *

class PreMatch(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('carrera', 'ciclo', 'sede', 'document')
