from django import forms

class BicicletaForm(forms.Form):
		marca = forms.CharField(max_length=100  )
		modelo = forms.CharField(max_length=100  )
		nro_serie = forms.CharField(max_length=100 )
		foto = forms.ImageField()
		processo_crime = forms.FileField()
		email = forms.EmailField(max_length=100)
