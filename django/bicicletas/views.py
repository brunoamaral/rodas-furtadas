from django.shortcuts import render

# Create your views here.
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Bicicleta
from .forms import BicicletaForm


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('bicicletas/home/index.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('bicicletas/home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('bicicletas/home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))

def reportar(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = BicicletaForm(request.POST, request.FILES)

		# check whether it's valid:
		if form.is_valid():
			marca = form.cleaned_data['marca']
			modelo = form.cleaned_data['modelo']
			nro_serie = form.cleaned_data['nro_serie']
			email = form.cleaned_data['email']
			foto = form.cleaned_data['foto']
			processo_crime = form.cleaned_data['processo_crime']
			bicicleta = Bicicleta.objects.create(
				marca = marca,
				modelo = modelo,
				nro_serie = nro_serie,
				email = email,
				foto=foto,
				processo_crime=processo_crime
			)
			bicicleta.save()

			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ''
	return render(request, 'bicicletas/home/index.html', {'form': form})
