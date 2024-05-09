from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10000000)], blank=True, null=True)