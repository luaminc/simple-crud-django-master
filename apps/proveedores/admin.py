from django.contrib import admin
from .models import CategoriaIndustria, Proveedor


# Register your models here.

@admin.register(CategoriaIndustria, Proveedor)
class BaseAdminRegister(admin.ModelAdmin):
    pass
