import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Ruche, Recolte
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('TP/management/csv/recolte.csv', header='infer')

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Convertir apiculteur_id en entier
            ruche_id = int(row['ruche_id'])

            # Récupérer l'instance Apiculteur correspondante
            ruche_instance = Ruche.objects.get(id=ruche_id)

            # Créer une instance Cheptel avec l'apiculteur correspondant
            mon_modele_instance = Recolte(
                ruche=ruche_instance,
                date = pd.to_datetime(row['date'], errors='coerce'),
                quantite = row ['quantite'],
         
            )
            instances_to_create.append(mon_modele_instance)

        # Bulk create des instances Cheptel
        Recolte.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))