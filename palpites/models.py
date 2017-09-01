# -*- coding: utf-8 -*-
from django.db import models

class Palpite(models.Model):
    autor = models.ForeignKey('auth.User', null=True)
    title = models.CharField(max_length=20)
    pj1c = models.IntegerField()
    pj1f = models.IntegerField()
    pj2c = models.IntegerField()
    pj2f = models.IntegerField()
    pj3c = models.IntegerField()
    pj3f = models.IntegerField()
    pj4c = models.IntegerField()
    pj4f = models.IntegerField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# Create your models here.
