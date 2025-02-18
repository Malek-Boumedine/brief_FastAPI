# Configuration (DB, JWT)
from dotenv import load_dotenv
import os

# Charger le fichier .env
load_dotenv(dotenv_path="./app/.env")

# Variables d'environnement globales
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./default.db")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
