from django.db import models

# Create your models here.

#Modelo para Categoria

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria =models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria
    
#Modelo para Videojuego

class Videojuego(models.Model):
    desarrollador = models.CharField(max_length=20, primary_key=True, verbose_name='Desarrollador')
    lanzamiento = models.CharField(max_length=10, verbose_name='Año Lanzamiento')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.desarrollador