from django.db import models
from django.contrib.auth.models import User 

class Apiculteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nom = models.CharField(max_length=255, default='default_value')
    prenom = models.CharField(max_length=255, default='default_value')
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.nom 
    