# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from usuarios.forms import UserModelForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
	form = UserModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			sucesso = "Parabéns! Você foi cadastrado com sucesso, efetue o login para entrar em campo."
			return render(request, '/login', )
	return render(request, 'usuarios/cadastro.html', context)

# Create your views here.
@login_required
def boleiros(request):
    boleiros = User.objects.all()
    return render(request, 'usuarios/boleiros.html', {'boleiros' : boleiros})


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/cadastro')
	return render(request, 'usuarios/login.html')

@login_required
def do_logout(request):
	logout(request)
	return redirect('/login')