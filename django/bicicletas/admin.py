from django.contrib import admin

# Register your models here.
from .models import *

# this class define which department columns will be shown in the department admin web site.
class BicicletaAdmin(admin.ModelAdmin):
	# a list of displayed columns name.
	list_display = ['nro_serie', 'marca','modelo','email']
	search_fields = ['nro_serie', 'email', 'marca','modelo' ]

admin.site.register(Bicicleta,BicicletaAdmin)

