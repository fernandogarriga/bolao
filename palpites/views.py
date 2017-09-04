# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from palpites.forms import PalpiteForm
from models import Palpite
from .forms import PalpiteForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def palpites_list(request):
    palpites = Palpite.objects.all().order_by('-total')

    #PONTUAÇÃO
    empate_certo = 5
    empate_errado = 3
    placar_certo = 5
    vencedor_certo = 3
    perdedor_certo = 2
    vencedor = 1

    # RESULTADO REAL DOS JOGOS

    rj1c = 2
    rj1f = 2
    rj2c = 2
    rj2f = 1
    rj3c = 2
    rj3f = 3
    rj4c = 0
    rj4f = 0

    vez = 2


    # CÁLCULO DA PONTUAÇÃO
    for palpite in palpites:
    	total = 0

    	pj1c = palpite.pj1c
    	pj1f = palpite.pj1f
        pj2c = palpite.pj2c
        pj2f = palpite.pj2f
        pj3c = palpite.pj3c
        pj3f = palpite.pj3f
        pj4c = palpite.pj4c
        pj4f = palpite.pj4f
    	

    	#CALCULA PONTUACAO


        #-----inicio------#

        if ((rj1c and rj1f) != "?"):

        	if ((pj1c == pj1f)and(rj1c == rj1f)):
        		if ((pj1c == rj1c)and(pj1f == rj1f)):
        			total = total+empate_certo
        		else: 
        			total = total+empate_errado	
        			

        	elif (pj1c > pj1f):
        		if (rj1c > rj1f):
        			if ((pj1c == rj1c)and(pj1f == rj1f)):
        				total = total+placar_certo
        			elif ((pj1c == rj1c)and(pj1f != rj1f)):
        				total = total+vencedor_certo
        			elif ((pj1c != rj1c)and(pj1f == rj1f)):
        				total = total+perdedor_certo
        			else:
        				total = total+vencedor
        		else:
        			total = total


        	else:
        		if (rj1c < rj1f):
        			if ((pj1c == rj1c)and(pj1f == rj1f)):
        				total = total+placar_certo
        			elif ((pj1c == rj1c)and(pj1f != rj1f)):
        				total = total+perdedor_certo
        			elif ((pj1c != rj1c)and(pj1f == rj1f)):
        				total = total+vencedor_certo
        			else:
        				total = total+vencedor
        		else:
        			total = total

            #-----fim------#


            #-----inicio------#
        if ((rj2c and rj2f) != "?"):

            if ((pj2c == pj2f)and(rj2c == rj2f)):
                if ((pj2c == rj2c)and(pj2f == rj2f)):
                    total = total+empate_certo
                else: 
                    total = total+empate_errado 
                    

            elif (pj2c > pj2f):
                if (rj2c > rj2f):
                    if ((pj2c == rj2c)and(pj2f == rj2f)):
                        total = total+placar_certo
                    elif ((pj2c == rj2c)and(pj2f != rj2f)):
                        total = total+vencedor_certo
                    elif ((pj2c != rj2c)and(pj2f == rj2f)):
                        total = total+perdedor_certo
                    else:
                        total = total+vencedor
                else:
                    total = total


            else:
                if (rj2c < rj2f):
                    if ((pj2c == rj1c)and(pj2f == rj2f)):
                        total = total+placar_certo
                    elif ((pj2c == rj2c)and(pj2f != rj2f)):
                        total = total+perdedor_certo
                    elif ((pj2c != rj2c)and(pj2f == rj2f)):
                        total = total+vencedor_certo
                    else:
                        total = total+vencedor
                else:
                    total = total

            #-----fim------#






        p = Palpite.objects.get(id = palpite.id)
        p.total = total
        p.save()

    	palpite.total = total
        

    
    return render(request, 'palpites/palpite_list.html', {'palpites' : palpites})


@login_required
def cadastro_palpites(request):
	form = PalpiteForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			palpite = form.save(commit=False)
			palpite.autor = request.user
			palpite.save()
			form.save()

			return redirect('/palpites')
	return render(request, 'palpites/cadastro_palpites.html', context)