from django.contrib import admin
# Register your models here.
from . models import*
from import_export.admin import ImportExportModelAdmin
@admin.register(Student)
class ViewAdmin(ImportExportModelAdmin):
    pass