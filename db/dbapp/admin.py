from django.contrib import admin

# Register your models here.
from dbapp.models import dbmodel
admin.site.register(dbmodel)