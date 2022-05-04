from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from bicicletas import views

urlpatterns = [
		# Matches any html file

		path('reportar/', views.reportar, name='reportar'),
		re_path(r'^.*\.*', views.pages, name='pages'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)