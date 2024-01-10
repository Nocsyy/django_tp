from django.db import models

class Intervention (models.Model):
    SUPPRESSION_CELLULES_ROYALES = 'Suppression des cellules royales'
    CHECK_SANTE = 'Check de santé'
    RECOLTE = 'Récolte'
    DISTRIBUTION_SIROP = 'Distribution de sirop'
    POSE_HAUSSES = 'Pose de hausses'
    DESTRUCTION = 'Destruction'
    MULTIPLICATION_ARTIFICIELLE = 'Multiplication artificielle de l\'essaim'
    TRAITEMENT = 'Traitement (apivar, acide oxalique, antifongique, ...)'

    NATURE_CHOICES = [
        (SUPPRESSION_CELLULES_ROYALES, 'Suppression des cellules royales'),
        (CHECK_SANTE, 'Check de santé'),
        (RECOLTE, 'Récolte'),
        (DISTRIBUTION_SIROP, 'Distribution de sirop'),
        (POSE_HAUSSES, 'Pose de hausses'),
        (DESTRUCTION, 'Destruction'),
        (MULTIPLICATION_ARTIFICIELLE, 'Multiplication artificielle de l\'essaim'),
        (TRAITEMENT, 'Traitement (apivar, acide oxalique, antifongique, ...)'),
    ]


    ruche =  models.ForeignKey('Ruche', on_delete=models.CASCADE, related_name='interventions')
    date = models.DateField()
    nature = models.CharField(choices=NATURE_CHOICES)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'intervention'
        verbose_name_plural = 'interventions'