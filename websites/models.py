# -*- coding: utf-8 -*-
from django.db import models

class Website(models.Model):
    url         = models.URLField(max_length=255, unique=True)
    title       = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture     = models.CharField(max_length=255)

