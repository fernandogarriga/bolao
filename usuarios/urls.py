from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^cadastro/$', views.cadastro, name='cadastro'),
	url(r'^boleiros/$', views.boleiros, name='boleiros'),
	url(r'^login/$', views.do_login, name='login'),
	url(r'^$', views.do_login, name='index'),
	url(r'^logout/$', views.do_logout, name='logout'),
]