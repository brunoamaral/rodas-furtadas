from django.db import models

# Create your models here.
class Bicicleta(models.Model):
	id = models.AutoField(primary_key=True)
	marca = models.CharField(max_length=280, blank=True, null=True)
	modelo = models.CharField(max_length=280, blank=True, null=True)
	nro_serie = models.CharField(max_length=280, blank=True, null=True, unique=True)
	foto = models.ForeignKey('Fotos', models.CASCADE, db_column='foto', blank=True, null=True)
	processo_crime = models.ForeignKey('Documentos', models.CASCADE, db_column='processo_crime', blank=True, null=True)
	email = models.EmailField(max_length=280, unique=False, null=False,blank=False)


class Documentos(models.Model):
	documento = models.FileField(upload_to='documents/')
	data = models.DateTimeField(auto_now_add=True)
	class Meta:
		managed = True
		verbose_name_plural = 'Documentos'


class Fotos(models.Model):
	foto = models.FileField(upload_to='documents/')
	data = models.DateTimeField(auto_now_add=True)
	class Meta:
		managed = True
		verbose_name_plural = 'Fotos'


