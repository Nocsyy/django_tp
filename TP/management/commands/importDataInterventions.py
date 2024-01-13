import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Ruche, Intervention
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
       
        data = pd.read_csv('TP/management/csv/intervention.csv', header='infer')

        instances_to_create = []

 
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
         
            ruche_id = int(row['ruche_id'])

           
            ruche_instance = Ruche.objects.get(id=ruche_id)

          
            mon_modele_instance = Intervention(
                ruche=ruche_instance,
                date = pd.to_datetime(row['date'], errors='coerce'),
                nature = row ['nature'],
                description = row ['description']
            )
            instances_to_create.append(mon_modele_instance)

       
        Intervention.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))