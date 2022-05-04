from django import forms

class ReportarBicicleta(forms.Form):
		marca = forms.CharField(max_length=100  )
		modelo = forms.CharField(max_length=100  )
		nro_serie = forms.CharField(max_length=100 )
		# foto = forms.
		# processo_crime = forms.
		email = forms.EmailField(max_length=100)
