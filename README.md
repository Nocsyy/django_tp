# TP Apiculteur Andy

# Description

L'objectif de ce projet est de créer une application dédiée à l'apiculture, offrant aux apiculteurs une plateforme complète pour gérer leur cheptel de ruches tout en mettant à disposition publiquement les données relatives aux ruches et aux abeilles.

## Fonctionnalités Principales

1. **Gestion du Cheptel de Ruches :**
   - Utilisation de vues et templates avec Jinja2 pour permettre aux apiculteurs de naviguer au sein de leur cheptel de ruches.
   - Mise en place de fonctionnalités telles que l'ajout, la modification et la suppression de ruches.

2. **API Publique :**
   - Utilisation de Django Rest Framework (DRF) pour créer une API robuste.
   - Utilisation de Serializers, ModelViewSet et Filtres DRF pour organiser et exposer les données des ruches et des abeilles.
   - Les données seront rendues publiques, permettant à d'autres applications ou plateformes de les utiliser.

3. **Architecture du Projet :**
   - Une architecture soigneusement planifiée avec des modèles bien définis pour les ruches, les abeilles, etc.
   - Utilisation de l'environnement virtuel pour isoler les dépendances du projet.
   - Développement d'une structure propre et organisée avec des applications Django distinctes pour une gestion modulaire.

4. **Backend uniquement, avec possibilité d'extension Frontend :**
   - Bien que le focus soit sur le backend, envisagez l'extension future en développant un frontend qui pourra tirer parti de l'API publique.

## Guideline pour le Développement

1. **Initialisation du Projet :**
   - Création d'un environnement virtuel.
   - Initialisation du projet Django et configuration de Git.

2. **Mise en Place du Projet et des Apps :**
   - Création des applications Django nécessaires pour la gestion des ruches.

3. **V1 Simplifiée des Modèles :**
   - Définition des modèles de base pour les ruches et les abeilles.

4. **Briques Logicielles Indispensables :**
   - Mise en place des API avec DRF.
   - Implémentation de l'authentification et des mesures de sécurité nécessaires.

5. **Développement Progressif :**
   - Ajout progressif des fonctionnalités manquantes en respectant une approche incrémentale.

Ce projet vise à fournir une solution complète et extensible pour les apiculteurs tout en respectant les bonnes pratiques de développement Django et en anticipant une évolution vers un frontend dans le futur.

# Installation

## 1. Cloner le Projet

   **Clonez le projet depuis GitHub sur votre machine locale.**

    
       git clone https://github.com/Nocsyy/django_tp.git
   
    
## 2. Environnement Virtuel

   Créez un environnement virtuel pour isoler les dépendances du projet.

    
    python -m venv venv
    
   Activez l'environnement virtuel.

   Sur Windows : 
  
    venv\Scripts\activate
    
   Sur MacOS/Linux : 
    
    source venv/bin/activate
   
## 4. Installation des Dépendances
   Connectez vous a votre base de donnée, n'oubliez pas de créer un .env à la racine du projet en suivant le fichier env-templates
    
    
## 5. Installation des Dépendances
   Installez les dépendances du projet.
    
    pip install -r requirements.txt
   

## 6. Configuration de la Base de Données
   Appliquez les migrations pour créer la base de données.
    
      python manage.py showmigrations
   Puis : 
   
      python manage.py migrate
   
## 7. Import des données 
   Téléchargez le dossier contenant les csv, puis placer le dans dossier management 
   Ensuite, dans l'ordre, importez les données avec les commandes suivantes : 
   1:
   
      python manage.py importDataUser
   2: 
   
    python manage.py importDataApiculteur
   3: 
   
    python manage.py importDataCheptel
   4: 
   
    python manage.py importDataRuche
   5: 
   
    python manage.py importDataContamination
   6: 
   
    python manage.py importDataInterventions
   7:
   
    python manage.py importDataRecolte
    

## 8. Création d'un Superutilisateur

   Créez un superutilisateur pour accéder à l'interface d'administration Django.

     python manage.py createsuperuser

## 9. Lancement du serveur 
   Lancez le serveur de développement.


    python manage.py runserver
  

# Table des Matières

- [TP Apiculteur Andy](#tp-apiculteur-andy)
- [Description](#description)
  - [Fonctionnalités Principales](#fonctionnalités-principales)
  - [Guideline pour le Développement](#guideline-pour-le-développement)
- [Installation](#installation)
  - [1. Cloner le Projet](#1-cloner-le-projet)
  - [2. Environnement Virtuel](#2-environnement-virtuel)
  - [4. Installation des Dépendances](#4-installation-des-dépendances)
  - [5. Installation des Dépendances](#5-installation-des-dépendances)
  - [6. Configuration de la Base de Données](#6-configuration-de-la-base-de-données)
  - [7. Import des données](#7-import-des-données)
  - [8. Création d'un Superutilisateur](#8-création-dun-superutilisateur)
  - [9. Lancement du serveur](#9-lancement-du-serveur)
- [Table des Matières](#table-des-matières)



[Expliquez comment installer votre projet de manière claire et concise. Assurez-vous d'inclure toutes les dépendances nécessaires et les étapes d'installation.]
