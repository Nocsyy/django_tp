# Generated by Django 5.0.1 on 2024-01-11 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TP', '0004_remove_user_nom_remove_user_prenom_apiculteur_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheptel',
            name='apiculteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TP.apiculteur'),
        ),
    ]