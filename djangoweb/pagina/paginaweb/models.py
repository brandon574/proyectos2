from django.db import models


class usuarios(models.Model):
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    correo=models.EmailField(max_length=20)
    curp=models.IntegerField(primary_key=True)
    usuario=models.CharField(max_length=10)
    correo_Asignado=models.EmailField(max_length=40,null=True)
    contraseña=models.CharField(max_length=40,null=False)

    





    