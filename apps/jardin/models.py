from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(verbose_name="Nombre/s", max_length=30)
    apellido=models.CharField(verbose_name="Apellido/s", max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "empleado"
        ordering = ["id"]
        
    def get_model_fields(model):
        return model._meta.fields