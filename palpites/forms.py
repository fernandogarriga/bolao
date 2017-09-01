# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Palpite


class PalpiteForm(forms.ModelForm):
	autor = forms.CharField(widget=forms.HiddenInput(), initial="aaa")
	title = forms.CharField(widget=forms.TextInput())
	pj1c = forms.IntegerField()
	pj1f = forms.IntegerField()
	pj2c = forms.IntegerField()
	pj2f = forms.IntegerField()
	pj3c = forms.IntegerField()
	pj3f = forms.IntegerField()
	pj4c = forms.IntegerField()
	pj4f = forms.IntegerField()
	class Meta:
		model = Palpite
		fields = ['title', 'pj1c', 'pj1f', 'pj2c', 'pj2f' , 'pj3c', 'pj3f', 'pj4c', 'pj4f']
		widgets = {
			'autor': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 20}),
			'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 20}),
			'pj1c': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj1f': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj2c': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj2f': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj3c': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj3f': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj4c': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
			'pj4f': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2})
		}

		

	