# Sydoni'Drive

## Description du Projet
Une application de covoiturage développée en Python avec une interface graphique Tkinter, permettant aux automobilistes de publier des trajets et aux passagers de les réserver. Le projet est structuré avec un backend pour la logique métier et un frontend pour l'interface utilisateur.

## Fonctionnalités
- Inscription et connexion des utilisateurs (automobilistes et passagers)
- Publication de trajets par les automobilistes (avec gestion des places et de l'engin)
- Recherche et réservation de trajets par les passagers
- Géolocalisation et affichage des trajets sur une carte (via `tkintermapview`)
- Gestion de l'historique des trajets pour les deux rôles
- Système de points pour les automobilistes (basé sur la publication et la réalisation de trajets)
- Possibilité de noter les trajets pour les passagers
- Basculement de rôle (automobiliste/passager) pour un même utilisateur

## Technologies Utilisées
- Python 3.11+
- Tkinter (pour l'interface graphique)
- `tkintermapview` (pour l'affichage des cartes)
- Fichiers JSON pour le stockage des données (utilisateurs, annonces, historiques)

## Installation

Pour installer et exécuter Sydoni'Drive sur votre machine locale, suivez ces étapes :

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/votre-nom-utilisateur/sydoni_Drive_project_final.git
    cd sydoni_Drive_project_final
    ```
    *(Remplacez `votre-nom-utilisateur` par votre nom d'utilisateur GitHub. )*

2.  **Créer et activer un environnement virtuel :**
    Il est fortement recommandé d'utiliser un environnement virtuel pour gérer les dépendances du projet.

    *   **Sur Windows :**
        ```bash
        python -m venv sydoni_env
        .\sydoni_env\Scripts\activate
        ```

    *   **Sur macOS/Linux :**
        ```bash
        python3 -m venv sydoni_env
        source sydoni_env/bin/activate
        ```

3.  **Installer les dépendances :**
    Une fois l'environnement virtuel activé, installez toutes les bibliothèques nécessaires à partir du fichier `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

4.  **Installer Tkinter (si nécessaire, pour Linux) :**
    Si vous êtes sur un système Linux et que vous rencontrez des erreurs liées à Tkinter, vous devrez peut-être installer le paquet `python3-tk` :
    ```bash
    sudo apt-get update
    sudo apt-get install python3-tk
    ```

## Utilisation

Pour lancer l'application, assurez-vous que votre environnement virtuel est activé et exécutez le fichier `main.py` :

```bash
python sydoni_Drive_project/sydoni_Drive/main.py
