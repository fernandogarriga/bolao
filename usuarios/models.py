# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver

from random import choice
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    telefone = models.IntegerField(blank='True', null='True', default='99999999')
    avatar = models.ImageField(upload_to='avatar', blank='True', null='True')
    status = models.BooleanField(default=False)



def set_token(self):
    self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])




def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)
    self.set_token()