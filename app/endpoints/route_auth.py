# Routes auth
from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Union, Annotated
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.utils import db_dependency, bcrypt_context, oauth2_bearer, create_access_token, verify_token, get_password_hash, verify_password, authenticate_user
from app.modeles import Users
from app.schemas import Token, TokenData, UserDB


router = APIRouter(prefix="/auth", tags=["auth"])

    


@router.post("/login")    # pour récupérer le token d'accès
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency) :
    user = authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user : 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nom d'utilisateur ou mot de passe incorrect", Headers={"WWW-Authenticate": "Bearer"})
    token_data = {
        "sub": user.email,
        "extra" : {
            "nom_banque": user.nom_banque,
            "role": user.role
        }
    }
    acces_token = create_access_token(data=token_data)
    return {"access_token": acces_token, "token_type": "bearer"}

 

def modify_password(new_password : str, db : db_dependency) -> UserDB : 
    
    pass


@router.post("/activation")   # pour activer le compte et changer le mot de passe à la premiere connexion
def activation() : 
    
    
    pass




@router.post("/logout")   # pour se déconnecter
def logout() : 
    pass



