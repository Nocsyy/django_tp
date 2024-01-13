import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Apiculteur
from django.contrib.auth.models import User
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('TP/management/csv/apiculteur.csv')

        instances_to_create = []

       
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Convertir user_id en entier
            user_id = int(row['user_id'])

        
            user_instance, created = User.objects.get_or_create(id=user_id)

    
            apiculteur_instance, apiculteur_created = Apiculteur.objects.get_or_create(user=user_instance)

            
            if not apiculteur_created:
                apiculteur_instance.nom = row['nom']
                apiculteur_instance.prenom = row['prenom']
                apiculteur_instance.contact = row['contact']
                apiculteur_instance.save()
            else:

                mon_modele_instance = Apiculteur(
                    user=user_instance,
                    nom=row['nom'],
                    prenom=row['prenom'],
                    contact=row['contact'],
                )
                instances_to_create.append(mon_modele_instance)


        Apiculteur.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))