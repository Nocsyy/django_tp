from django.db import models
from ..models import Apiculteur

class Cheptel(models.Model): 
    nom = models.CharField(max_length=100)
    apiculteur = models.ForeignKey('Apiculteur', on_delete=models.CASCADE, related_name='cheptels')
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'cheptel'
        verbose_name_plural = 'cheptels'