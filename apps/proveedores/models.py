from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class BaseName(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
       
    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    

class CategoriaIndustria(BaseName):
    #descripcion_industria = models.CharField(max_length=100, verbose_name='Nombre Categoria') //ya hereda un nombre desde BaseName

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Proveedor(BaseName):
    rut = models.CharField(max_length=20, unique=True, verbose_name='RUT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    pais = models.CharField(max_length=100, verbose_name='País')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    correo = models.EmailField(max_length=254, verbose_name='Correo electrónico')
    image = models.ImageField(upload_to='proveedor', verbose_name='Imagen')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    category = models.ForeignKey(CategoriaIndustria, on_delete=models.CASCADE, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def get_edit_url(self):
        return reverse_lazy('proveedores:proveedores-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('proveedores:proveedores-delete', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('proveedores:proveedores-detail', kwargs={'pk': self.pk})
