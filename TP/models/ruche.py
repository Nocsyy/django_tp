from django.db import models

class Ruche(models.Model): 
    STATUT_CHOICES = [
        ('Active', 'Active'),
        ('En attente', 'En attente'),
        ('Detruite', 'Détruite'),
    ]
    
    TYPE_ABEILLE_CHOICES = [
        ('Apis mellifera', 'Apis mellifera (Abeille européenne)'),
        ('Apis cerana', 'Apis cerana (Abeille asiatique)'),
        ('Apis mellifera mellifera', 'Apis Mellifera Mellifera (Abeille noire)'),
        ('Apis mellifera ligustica', 'Apis Mellifera Ligustica (Abeille italienne)'),
        ('Apis mellifera caucasica', 'Apis mellifera caucasica (Abeille caucasienne)'),
        ('Apis mellifera carnica', 'Apis mellifera carnica (Abeille carolienne)'),
        ('Abeille buckfast', 'L\'abeille Buckfast'),
        ('Abeille charpentière xylocope', 'L\'abeille charpentière xylocope'),
        ('Autre', 'Autre')
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