import pandas as pd
from django.core.management.base import BaseCommand
from TP.models import Apiculteur
from tqdm import tqdm
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # Charger le fichier CSV avec pandas
        data = pd.read_csv('TP/management/csv/user.csv')

        data = data.fillna('1970-01-01')

        instances_to_create = []

        # Iterer sur les lignes du dataframe et ajouter les instances à la liste
        for index, row in tqdm(data.iterrows(), desc='Importation des données', total=len(data)):
            # Créer un utilisateur Django
            mon_modele_instance = User(
                password=row['password'],
                last_login=pd.to_datetime(row['last_login'], errors='coerce'),
                is_superuser=row['is_superuser'],
                username=row['username'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                is_staff=row['is_staff'],
                is_active=row['is_active'],
                date_joined=pd.to_datetime(row['date_joined'], errors='coerce'),
            )
            instances_to_create.append(mon_modele_instance)

        User.objects.bulk_create(instances_to_create)

        self.stdout.write(self.style.SUCCESS('Données importées avec succès.'))