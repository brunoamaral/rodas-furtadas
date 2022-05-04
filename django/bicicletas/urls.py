from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from bicicletas import views

urlpatterns = [
		# Matches any html file
		re_path(r'^.*\.*', views.pages, name='pages'),
		path('reportar/', views.reportar, name='reportar'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


