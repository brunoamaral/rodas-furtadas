from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

fs = FileSystemStorage(location='/media/')

def file_size(value): # add this to some file where you can import it from
	limit = 1 * 1024 * 1024
	if value.size > limit:
			raise ValidationError('Os ficheiros não podem ser maiores do que 1 Mb.')


# Create your models here.
class Bicicleta(models.Model):
	RAZOES = [('pertence-me e foi roubada', 'Pertence-me e foi roubada'),('não me pertence, encontrei-a','Não me pertence, encontrei-a')]

	id = models.AutoField(primary_key=True)
	marca = models.CharField(max_length=280, blank=True, null=True)
	modelo = models.CharField(max_length=280, blank=True, null=True)
	nro_serie = models.CharField(max_length=280, blank=True, null=True, unique=True)
	foto = models.ImageField(storage=fs,
	blank=False, null=False,
	validators=[file_size,FileExtensionValidator(['jpg','jpeg'])]
	)
	comprovativo = models.FileField(storage=fs,
	blank=True, null=True,
	validators=[file_size,FileExtensionValidator(['pdf','jpeg','jpg'])]
	)
	email = models.EmailField(max_length=280, unique=False, null=False,blank=False)
	valid = models.BooleanField(default=False, blank=False,null=False)
	razao_registo = models.CharField(choices=RAZOES, max_length=50, default=RAZOES[0][0])
