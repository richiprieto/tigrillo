from django.db import models
from django import forms


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.question_text

class Profesiones(models.Model):
    prof_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.prof_text

class Carrera(models.Model):
    c1 = "ing"
    c2 = "ing2"

    c_choices = ((c1, u"ing"),(c2, u"ing2"))
    c = forms.ChoiceField(choices = c_choices)

    def __str__(self):
        return self.c

class Ciclo(models.Model):
    ciclo_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.ciclo_text

class Repeticion(models.Model):
    repeticion_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.repeticion_text

class Choice(models.Model):
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE)
    ciclo= models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
