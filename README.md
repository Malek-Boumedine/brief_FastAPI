# API de Prédiction de Prêts

Une API REST développée avec FastAPI pour la gestion et la prédiction de prêts bancaires. Cette application permet aux institutions bancaires de soumettre des demandes de prêts et d'obtenir une prédiction sur l'accord ou le refus du prêt en utilisant un modèle de machine learning CatBoost.

### Dépendances principales

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-00a393.svg)
![SQLModel](https://img.shields.io/badge/SQLModel-0.0.8+-red.svg)
![Alembic](https://img.shields.io/badge/Alembic-1.12.0+-yellow.svg)
![CatBoost](https://img.shields.io/badge/CatBoost-1.2+-green.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243.svg)
![JWT](https://img.shields.io/badge/JWT-Python--Jose-blue.svg)
![Passlib](https://img.shields.io/badge/Passlib-1.7.4+-lightgrey.svg)
![PyMySQL](https://img.shields.io/badge/PyMySQL-1.1.0+-orange.svg)

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Development-red.svg)

## Fonctionnalités Principales

- Authentification JWT
- Gestion des utilisateurs (banques)
- Prédiction de l'accord de prêts via modèle ML
- Historique des demandes de prêts
- Système de rôles (admin/user)

## Prérequis

- Python 3.11+
- MariaDB (optionnel, SQLite par défaut)
- Packages système requis :
  - Ouvrez un terminal et exécutez la commande suivante :
  ```bash
  sudo apt-get install libmariadb-dev libmariadb-dev-compat pkg-config
  ```

## Installation

1. Cloner le repository
2. Créer un environnement virtuel :
- Ouvrez un terminal et exécutez la commande suivante :

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Installer les dépendances :
- Ouvrez un terminal et exécutez la commande suivante :
    ```bash
    pip install -r requirements.txt
    ```

4. Configurer les variables d'environnement dans `.env`

Créer un fichier `.env` avec :

```ini
SECRET_KEY="votre_clé_secrète"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL="sqlite:///./test.db"  # ou URL MariaDB
```

5. extrayez le fichier best_cat_boost.tar.xz.
- Ouvrez un terminal et exécutez la commande suivante :
```bash
tar -xvf best_cat_boost.tar.xz
```
Pour générer une clé secrète :
- Ouvrez un terminal et exécutez la commande suivante :
```bash
openssl rand -hex 32
```

## Configuration de la Base de Données

### SQLite (par défaut)
Avant de démarrer l'API, exécutez python populate_db.py pour créer et remplir la base de données.

### MariaDB (optionnel)
1. Se connecter à MariaDB en tant que root
2. Créer l'utilisateur de la base de données :
- Ouvrez un terminal et exécutez la commande suivante :
    ```sql
    CREATE USER 'utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';
    GRANT ALL PRIVILEGES ON *.* TO 'utilisateur'@'localhost';
    FLUSH PRIVILEGES;
    ```

## Utilisateurs par défaut
Après l'exécution de `populate_db.py`, les identifiants suivants seront disponibles :
- Admin :
  - Email : admin
  - Mot de passe : admin

## Migrations avec Alembic
1. Initialiser Alembic :
- Ouvrez un terminal et exécutez la commande suivante :
    ```bash
    alembic init alembic
    ```

2. Générer une migration :
- Ouvrez un terminal et exécutez la commande suivante :
   
    ```bash
    alembic revision --autogenerate -m "description"
    ```

3. Appliquer les migrations :
- Ouvrez un terminal et exécutez la commande suivante :
    ```bash
    alembic upgrade head
    ```

## Structure du Projet

```
.
├── alembic/            # Fichiers de migration
├── app/
│   ├── endpoints/      # Routes API
│   ├── database.py    # Configuration DB
│   ├── ml.py         # Logique ML
│   ├── modeles.py    # Modèles DB
│   ├── schemas.py    # Schémas Pydantic
│   └── utils.py      # Utilitaires
├── main.py           # Point d'entrée
└── requirements.txt  # Dépendances
```

## Points d'API Principaux

#### Authentication
- `POST /auth/login` : Obtention du token JWT
- `POST /auth/activation` : Activation du compte

#### Administration
- `GET /admin/users` : Liste des utilisateurs
- `POST /admin/users` : Création d'utilisateur

#### Prêts
- `POST /loans/request` : Demande de prêt
- `GET /loans/history` : Historique des demandes

## Sécurité
- Authentification via JWT
- Mots de passe hashés avec bcrypt
- Système de rôles (admin/user)
- Durée de validité configurable des tokens

## Machine Learning
Le modèle de prédiction utilise CatBoost et est chargé depuis best_cat_boost.pkl, fichier extrait à l'étape 5

## Démarrage

```bash
uvicorn main:app --reload
```

L'API sera accessible sur [http://localhost:8000](http://localhost:8000)

- **Documentation Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs)

### Exemples d'utilisation

```bash
# Authentification
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=admin"

# Demande de prêt (nécessite un token JWT)
curl -X POST "http://localhost:8000/loans/request" \
     -H "Authorization: Bearer votre_token_jwt" \
     -H "Content-Type: application/json" \
     -d '{
           "City": "SPRINGFIELD",
           "State": "TN",
           ...
         }'
```

## Dépannage
- Si l'erreur "Module not found" apparaît, vérifiez que vous êtes bien dans l'environnement virtuel
- Pour les problèmes de base de données, vérifiez les permissions et les identifiants dans le fichier .env
- Si le modèle ML ne se charge pas, vérifiez que le fichier best_cat_boost.pkl a bien été extrait

### Contribution
Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## Licence
MIT License

Copyright (c) 2025 malek_khadija

L'autorisation est accordée, gracieusement, à toute personne obtenant une copie
de ce logiciel et des fichiers de documentation associés (le "Logiciel"), de traiter
le Logiciel sans restriction, notamment sans limitation les droits
d'utiliser, de copier, de modifier, de fusionner, de publier, de distribuer, de sous-licencier,
et/ou de vendre des copies du Logiciel, ainsi que d'autoriser les personnes auxquelles le
Logiciel est fourni à le faire, sous réserve des conditions suivantes :

La notice de copyright ci-dessus et cette notice d'autorisation doivent être incluses dans
toutes les copies ou parties substantielles du Logiciel.

LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPLICITE OU IMPLICITE,
NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET
D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU TITULAIRES DU DROIT D'AUTEUR NE
SERONT RESPONSABLES DE TOUT DOMMAGE, RÉCLAMATION OU AUTRE RESPONSABILITÉ, QUE CE SOIT DANS
LE CADRE D'UN CONTRAT, D'UN DÉLIT OU AUTRE, EN PROVENANCE DE, CONSÉCUTIF À OU EN RELATION
AVEC LE LOGICIEL OU SON UTILISATION, OU AVEC D'AUTRES ÉLÉMENTS DU LOGICIEL.
