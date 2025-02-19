## installer les paquets nécessaires : 

`sudo apt-get install libmariadb-dev libmariadb-dev-compat pkg-config`


# pour créer l'utilisateur de la BDD
```
CREATE USER 'loanapi'@'localhost' IDENTIFIED BY '0664080295Malek';
GRANT ALL PRIVILEGES ON loan.* TO 'loanapi'@'localhost';
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

