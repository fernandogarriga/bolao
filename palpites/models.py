# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Palpite(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)
    pj1c = models.CharField(max_length=2)
    pj1f = models.CharField(max_length=2)
    pj2c = models.CharField(max_length=2)
    pj2f = models.CharField(max_length=2)
    pj3c = models.CharField(max_length=2)
    pj3f = models.CharField(max_length=2)
    pj4c = models.CharField(max_length=2)
    pj4f = models.CharField(max_length=2)

    def __str__(self):
        return self.title

# Create your models here.
