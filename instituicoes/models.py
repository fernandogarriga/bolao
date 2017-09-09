# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image

class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    nome_curto= models.CharField(max_length=3)
    image = models.ImageField(upload_to='bandeiras', blank='True', null='True')



    def __str__(self):
        return self.nome_curto


# Create your models here.
