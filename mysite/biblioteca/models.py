from django.db import models

from django.db import models

# Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Modelo Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo


# Modelo Reseña
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    contenido = models.TextField()
    puntuacion = models.PositiveIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de '{self.libro.titulo}' - {self.puntuacion}/5"
