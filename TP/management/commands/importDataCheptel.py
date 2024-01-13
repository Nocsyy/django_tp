import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Cheptel, Apiculteur
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
       
        data = pd.read_csv('TP/management/csv/cheptel.csv', header='infer')

        instances_to_create = []

      
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Convertir apiculteur_id en entier
            apiculteur_id = int(row['apiculteur_id'])

           
            apiculteur_instance = Apiculteur.objects.get(id=apiculteur_id)

      
            mon_modele_instance = Cheptel(
                nom=row['nom'],
                apiculteur=apiculteur_instance,
            )
            instances_to_create.append(mon_modele_instance)

       
        Cheptel.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))