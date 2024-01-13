import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Cheptel, Ruche
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('TP/management/csv/ruche.csv', header='infer')

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Convertir apiculteur_id en entier
            cheptel_id = int(row['cheptel_id'])

            # Récupérer l'instance Apiculteur correspondante
            cheptel_instance = Cheptel.objects.get(id=cheptel_id)

            # Créer une instance Cheptel avec l'apiculteur correspondant
            mon_modele_instance = Ruche(
                nom = row ['nom'],
                statut = row ['statut'],
                date_statut = pd.to_datetime(row['date_statut'], errors='coerce'),
                annee_reine = row ['annee_reine'],
                type_abeille = row ['type_abeille'],
                contamination = row ['contamination'],
                cheptel=cheptel_instance,
              
         
            )
            instances_to_create.append(mon_modele_instance)

        # Bulk create des instances Cheptel
        Ruche.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))