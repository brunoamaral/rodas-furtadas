from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from bicicletas import views

urlpatterns = [
		path('reportar/', views.reportar, name='reportar'),
		# Matches any html file
		re_path(r'^.*\.*', views.pages, name='pages'),
] 

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)