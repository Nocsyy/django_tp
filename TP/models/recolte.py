from django.db import models

class Recolte (models.Model): 
    ruche = models.ForeignKey('Ruche', on_delete=models.CASCADE, related_name='recoltes')
    date = models.DateTimeField()
    quantite = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'recolte'
        verbose_name_plural = 'recoltes'