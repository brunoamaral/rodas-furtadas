from django import forms
from django.forms import ModelForm

from .models import Bicicleta

class BicicletaForm(ModelForm):
		# marca = forms.CharField(max_length=100  )
		# modelo = forms.CharField(max_length=100  )
		# nro_serie = forms.CharField(max_length=100 )
		# foto = forms.ImageField()
		# processo_crime = forms.FileField()
		# email = forms.EmailField(max_length=100)

	class Meta:
		model = Bicicleta
		fields = [
		'marca',
		'modelo',
		'nro_serie',
		'foto',
		'comprovativo',
		'email',
		'razao_registo'
		]
		exclude = ('valid',)




