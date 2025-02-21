# Routes admin
from fastapi import APIRouter
from app.schemas import CreateUserRequest
from app.utils import db_dependency, bcrypt_context
from app.modeles import Users
from sqlalchemy import text


router = APIRouter(prefix="/admin", tags=["admin"])  # pour les routes d'administration


@router.get("/users")   # Obtenir la liste des utilisateurs
def get_users(db : db_dependency):
    result = db.execute(text("SELECT * FROM users"))
    users = result.mappings().all()
    return users


@router.post("/users")  # Créer un utilisateur
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    create_user_model = Users(
        nom_banque=create_user_request.nom_banque,
        email=create_user_request.email, 
        hashed_password=bcrypt_context.hash(create_user_request.password)
        )
    db.add(create_user_model)
    db.commit()
    return {"message": f"Utilisateur {create_user_request.nom_banque} créé"}
    