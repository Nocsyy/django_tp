import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Cheptel, Apiculteur
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('TP/management/csv/cheptel.csv', header='infer')

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Convertir apiculteur_id en entier
            apiculteur_id = int(row['apiculteur_id'])

            # Récupérer l'instance Apiculteur correspondante
            apiculteur_instance = Apiculteur.objects.get(id=apiculteur_id)

            # Créer une instance Cheptel avec l'apiculteur correspondant
            mon_modele_instance = Cheptel(
                nom=row['nom'],
                apiculteur=apiculteur_instance,
            )
            instances_to_create.append(mon_modele_instance)

        # Bulk create des instances Cheptel
        Cheptel.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))