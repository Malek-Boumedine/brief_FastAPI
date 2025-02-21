# Routes admin
from fastapi import APIRouter, Depends
from app.schemas import CreateUserRequest
from app.utils import db_dependency, bcrypt_context, get_current_user
from app.modeles import Users
from sqlalchemy import text
from typing import Annotated


router = APIRouter(prefix="/admin", tags=["admin"])  # pour les routes d'administration


@router.get("/users")   # Obtenir la liste des utilisateurs
async def get_users(db : db_dependency, current_user: Annotated[Users, Depends(get_current_user)]):
    role = current_user.role
    if role == "admin" : 
        result = db.execute(text("SELECT * FROM users")).mappings().all()
        return result


@router.post("/users")  # Créer un utilisateur
async def create_user(create_user_request: CreateUserRequest, db: db_dependency, current_user: Annotated[Users, Depends(get_current_user)]):
    role = current_user.role
    if role == "admin" : 
        create_user_model = Users(
            nom_banque=create_user_request.nom_banque,
            email=create_user_request.email, 
            hashed_password=bcrypt_context.hash(create_user_request.password)
            )
        db.add(create_user_model)
        db.commit()
        return {"message": f"Utilisateur {create_user_request.nom_banque} créé"}
    