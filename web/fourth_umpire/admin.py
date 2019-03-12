from django.contrib import admin
#from .models import Match
from import_export.admin import ImportExportModelAdmin
from .models import *


#admin.site.register(Match)
@admin.register(DataSet, Match)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
