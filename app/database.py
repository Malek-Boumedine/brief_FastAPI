from sqlmodel import SQLModel, create_engine, text, Session
from dotenv import load_dotenv
import os
from .modeles import *



load_dotenv(dotenv_path="./app/.env")


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Par défaut SQLite si non défini

# Vérifier si on utilise MariaDB pour créer la base de données si nécessaire
if "mariadb" in DATABASE_URL:
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", None)
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", None)
    DB_NAME = "loan"

    # moteur pour créer la BDD
    temp_engine = create_engine(f"mariadb+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:3306/")

    with temp_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
        conn.execute(text("FLUSH PRIVILEGES"))
    temp_engine.dispose()

    DATABASE_URL = f"mariadb+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:3306/{DB_NAME}"  # BDD définitive sous mariadb

sqlite_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
engine = create_engine(DATABASE_URL, connect_args=sqlite_args)

SQLModel.metadata.create_all(engine)    # Crée les tables dans la base de données

def db_connection():
    session = Session(engine)  # Ouvre une session SQLModel
    try:
        yield session  # Garde la session ouverte pour l'API
    finally:
        session.close()  # Ferme la session après utilisation


