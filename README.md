# financial_data_companies_python_mongo_ETL
Ce projet met en œuvre un processus ETL pour extraire, transformer et charger les données financières de plusieurs entreprises dans une base de données MongoDB. La structure du projet est la suivante :
## Structure des Fichiers
1. `data_processing.py`:
Contient toutes les fonctions liées au processus ETL.
- extract_ticker() : Extrait les données financières de différentes entreprises en utilisant la bibliothèque yfinance.
- transform_data(df) : Transforme le DataFrame des données extraites en arrondissant les valeurs à deux décimales.
- load_mongo(df) : Charge les données transformées dans une base de données MongoDB.

2. `main.py`: Orchestre l'exécution complète du projet en appelant les fonctions appropriées dans data_processing.py.
S'assure que le processus d'ETL est effectué de manière complète.

3. `requirements.txt`: Liste toutes les dépendances nécessaires pour exécuter le projet.

## Configuration et prérequis

1. Installation des Dépendances :

Utilisez la commande suivante pour installer les bibliothèques Python nécessaires:
```bash
pip install -r requirements.txt 
```

