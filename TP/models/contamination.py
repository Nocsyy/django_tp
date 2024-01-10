from django.db import models

class Contamination(models.Model): 
    VARROA_DESTRUCTOR = 'Varroa destructor'
    LOQUE = 'Loque'
    NOSEMOSIS = 'Nosémose'
    MALADIE_NOIRE = 'Maladie noire'
    ACARIOSE = 'Acariose'
    AUTRES = 'Autres'
    
    MALADIE_CHOICES = [
        (VARROA_DESTRUCTOR, 'Varroa destructor'),
        (LOQUE, 'Loque'),
        (NOSEMOSIS, 'Nosémose'),
        (MALADIE_NOIRE, 'Maladie noire'),
        (ACARIOSE, 'Acariose'),
        (AUTRES, 'Autres'),
    ]
    ruche =  models.ForeignKey('Ruche', on_delete=models.CASCADE, related_name='contaminations')
    date = models.DateField()
    maladie = models.CharField(max_length=100, choices=MALADIE_CHOICES)
    traite = models.BooleanField()

    class Meta:
        verbose_name = 'contamination'
        verbose_name_plural = 'contaminations'