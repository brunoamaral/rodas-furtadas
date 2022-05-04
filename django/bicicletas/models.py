from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/fotos')

# Create your models here.
class Bicicleta(models.Model):
	id = models.AutoField(primary_key=True)
	marca = models.CharField(max_length=280, blank=True, null=True)
	modelo = models.CharField(max_length=280, blank=True, null=True)
	nro_serie = models.CharField(max_length=280, blank=True, null=True, unique=True)
	foto = models.ImageField(storage=fs,
	blank=False, null=False
	)
	processo_crime = models.FileField(storage=fs,
	blank=False, null=False
	)
	email = models.EmailField(max_length=280, unique=False, null=False,blank=False)



