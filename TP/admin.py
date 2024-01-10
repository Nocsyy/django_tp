from django.contrib import admin
from .models import Apiculteur, Cheptel, Contamination, Intervention, Recolte, Ruche, User


# Register your models here.
# Admin pour le modèle Animal avec des filtres avancés
class ApiculteurAdmin(admin.ModelAdmin):
   list_display = ('user',)
   search_fields = ('user',)
   


# Admin pour le modèle Species
class CheptelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'apiculteur')
    search_fields = ('nom',)
    list_filter = ('apiculteur',)


# Admin pour le modèle Zone
class ContaminationAdmin(admin.ModelAdmin):
    list_display = ('ruche', 'date', 'maladie', 'traite')
    search_fields = ('ruche',)
    list_filter = ('maladie', 'ruche', 'traite')
   

# Admin pour le modèle Keeper avec des filtres avancés
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('ruche', 'date', 'nature', 'description')
    search_fields = ('ruche',)
    list_filter = ('ruche', 'nature')

class RecolteAdmin(admin.ModelAdmin):
    list_display = ('ruche', 'date', 'quantite')
    search_fields = ('ruche',)

class RucheAdmin(admin.ModelAdmin):
    list_display = ('cheptel', 'nom', 'statut', 'date_statut', 'annee_reine', 'type_abeille', 'contamination')
    search_fields = ('nom',)
    list_filter = ('statut', 'type_abeille', 'cheptel')

class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom')
    search_fields = ('nom',)


# Enregistrement des modèles avec leurs configurations d'administration personnalisées
admin.site.register(Apiculteur, ApiculteurAdmin)
admin.site.register(Cheptel, CheptelAdmin)
admin.site.register(Contamination, ContaminationAdmin)
admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Recolte, RecolteAdmin)
admin.site.register(Ruche, RucheAdmin)
admin.site.register(User, UserAdmin)


