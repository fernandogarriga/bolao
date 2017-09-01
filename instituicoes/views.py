# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Instituicao

# Create your views here.

def instituicoes_list(request):
    instituicoes = Instituicao.objects.all
    return render(request, 'instituicoes/instituicao_list.html', {'instituicoes' : instituicoes})