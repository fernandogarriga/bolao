# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from usuarios.forms import UserModelForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from palpites.models import Palpite
from .forms import ProfileForm

from .models import Profile

from django.template.context_processors import csrf

def cadastro(request):
	form = UserModelForm(request.POST or None)
	form2 = ProfileForm(request.POST, request.FILES, prefix='profile')
	context = {'form':form, 'form2':form2}
	if request.method == 'POST':
		if form.is_valid() and form2.is_valid():
			user = form.save()
			

			#create entry for UserProfile (extension of new_user object)      
			profile = form2.save(commit = False)
			profile.user = User.objects.get(username=request.POST['username'])
			profile.save()
			sucesso = "Parabéns! Você foi cadastrado com sucesso, efetue o login para entrar em campo."
			return render(request, '/login')
	else:
		form = UserModelForm(prefix = "user")
		form2 = ProfileForm(prefix = "profile")
		c = {
			'form':form,
			'form2':form2,
			}
		c.update(csrf(request))
	return render(request, 'usuarios/cadastro.html', context)

# Create your views here.
@login_required
def boleiros(request):
	boleiros = User.objects.all().filter(profile__status=True)
	return render(request, 'usuarios/boleiros.html', {'boleiros' : boleiros})


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/cadastro')
	boleiros = User.objects.all()
	palpites = Palpite.objects.all()
	return render(request, 'usuarios/login.html', {'boleiros' : boleiros, 'palpites' : palpites})

@login_required
def do_logout(request):
	logout(request)
	boleiros = User.objects.all()
	palpites = Palpite.objects.all()
	return redirect('/login')









@login_required

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })