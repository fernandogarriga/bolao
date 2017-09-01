# -*- coding: utf-8 -*-
from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    nome_curto= models.CharField(max_length=3)

    def __str__(self):
        return self.nome_curto

# Create your models here.
