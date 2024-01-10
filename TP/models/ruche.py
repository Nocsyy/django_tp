from django.db import models

class Ruche(models.Model): 
    STATUT_CHOICES = [
        ('active', 'Active'),
        ('en_attente', 'En attente'),
        ('detruite', 'Détruite'),
    ]
    
    TYPE_ABEILLE_CHOICES = [
        ('apis_mellifera', 'Apis mellifera (Abeille européenne)'),
        ('apis_cerana', 'Apis cerana (Abeille asiatique)'),
        ('apis_mellifera_mellifera', 'Apis Mellifera Mellifera (Abeille noire)'),
        ('apis_mellifera_ligustica', 'Apis Mellifera Ligustica (Abeille italienne)'),
        ('apis_mellifera_caucasica', 'Apis mellifera caucasica (Abeille caucasienne)'),
        ('apis_mellifera_carnica', 'Apis mellifera carnica (Abeille carolienne)'),
        ('abeille_buckfast', 'L\'abeille Buckfast'),
        ('abeille_charpentière_xylocope', 'L\'abeille charpentière xylocope'),
        ('autre', 'Autre')
    ]

    cheptel = models.ForeignKey('Cheptel', on_delete=models.CASCADE, related_name='ruches')
    nom = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    date_statut = models.DateField()
    annee_reine = models.PositiveIntegerField()# 4 ans max 
    type_abeille = models.CharField(max_length=29, choices=TYPE_ABEILLE_CHOICES)
    contamination = models.BooleanField()

    def __str__(self):
        return f"{self.nom} ({self.get_statut_display()})"

    class Meta:
        verbose_name = 'ruche'
        verbose_name_plural = 'ruches'