from django.db import models

class Apiculteur(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    