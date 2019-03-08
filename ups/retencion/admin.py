from django.contrib import admin
from .models import Question
from .models import Profesiones
from .models import Ciclo
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Profesiones)
admin.site.register(Ciclo)
admin.site.register(Choice)
