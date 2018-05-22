# -*- coding: utf-8 -*-

from django.db import models

class Regex(models.Model):
    expresion = models.CharField(max_length=255, blank=True)

