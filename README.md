## installer les paquets nécessaires : 

`sudo apt-get install libmariadb-dev libmariadb-dev-compat pkg-config`


# pour créer l'utilisateur de la BDD (se connecter au serveur mariadb avec root)
```
CREATE USER 'utilisateur'@'localhost' IDENTIFIED BY 'mot de passe';
GRANT ALL PRIVILEGES ON *.* TO 'utilisateur'@'localhost';
FLUSH PRIVILEGES;
```


# pour les migrations : 
installer alembic
`pip install alembic`

Initialiser Alembicdans le répertoire principal du projet
`alembic init alembic`

Modifier le fichier alembic/env.py pour inclure le moteur SQLModel
```
from app.modeles import SQLModel
target_metadata = SQLModel.metadata
(à la place de target_metadata = None)
```

Après avoir modifié vos modèles dans modeles.py, générez une migration
`alembic revision --autogenerate -m "commentaire"`

si le changement n'est pas pris en compte (par exemple ajout d'une contrainte), il faut le spécifier dans les fonctions uopgrade() et downgrade() : 

- aller dans migrations/versions
- chercher le fichier portant le nom de la migtration qu'on crée avec `alembic revision --autogenerate -m "commentaire"`
- une fois les fonctions modifiées, executer `alembic upgrade head` pour appliquer la migration

## astuce : pour générer une clé secrete forte : 
taper cette commande dans un terminal `openssl rand -hex 32`

## extraire le fichier pkl du modele 
`best_cat_boost.tar.xz`