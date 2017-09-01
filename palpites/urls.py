from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^cadastro-palpites/$', views.cadastro_palpites, name='cadastro-palpites'),
]