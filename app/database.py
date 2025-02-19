from sqlmodel import SQLModel, create_engine, text, Session
from dotenv import load_dotenv
import os
from .modeles import *






load_dotenv(dotenv_path="./app/.env")

DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", None)
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", None)

# moteur pour créer la BDD
bdd_engine = create_engine(f"mariadb+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:3306/")
# DB_NAME = "loan"
DB_NAME = "khad"

with bdd_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.execute(text("FLUSH PRIVILEGES"))


# URL finale vers la BDD
DATABASE_URL = f"mariadb+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:3306/{DB_NAME}"

# moteur pour la BDD définitive
engine = create_engine(DATABASE_URL)

# DB test
database_test = "sqlite:///./test.db"
engine_test = create_engine(database_test, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine_test)
session = Session(engine_test)


def db_connection():
    with engine_test.connect() as connexion:
        yield connexion





