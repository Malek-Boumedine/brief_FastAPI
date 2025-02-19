# Point d'entrée de l'application
from sqlmodel import SQLModel
from app.database import engine
# import app.modeles


# Créer les tables dans la base de données
SQLModel.metadata.create_all(engine)