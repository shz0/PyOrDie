from django.core.exceptions import ValidationError
from django.db import models

class Artikel(models.Model):
    titel = models.CharField(max_length=8)
    beschreibung = models.TextField(null=True, blank=True)
    lagerort = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titel