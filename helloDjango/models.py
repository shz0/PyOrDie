from django.db import models

class Artikel(models.Model):
    titel = models.CharField(max_length=100)
    number = models.TextField(null=True, blank=True)

