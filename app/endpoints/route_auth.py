# Routes auth
from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import text
from typing import Annotated
from app.utils import db_dependency, get_current_user, create_access_token, get_password_hash, authenticate_user
from app.modeles import Users
from app.schemas import NewPassword


router = APIRouter(prefix="/auth", tags=["auth"])

    


@router.post("/login")    # pour récupérer le token d'accès
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency) :
    """
    Authentifie un utilisateur et génère un token JWT d'accès.

    Args:
        form_data (OAuth2PasswordRequestForm): Formulaire contenant username (email) et password.
        db (Session): Session de base de données SQLAlchemy.

    Returns:
        dict: Token d'accès JWT et son type.
            Format: {"access_token": str, "token_type": "bearer"}

    Raises:
        HTTPException:
            - 401: Si les identifiants sont incorrects
            - 404: Si l'utilisateur n'existe pas

    Note:
        Le token généré contient l'email, le nom de la banque et le rôle de l'utilisateur
    """
    user = authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user : 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nom d'utilisateur ou mot de passe incorrect", headers={"WWW-Authenticate": "Bearer"})
    token_data = {
        "sub": user.email,
        "extra" : {
            "nom_banque": user.nom_banque,
            "role": user.role
        }
    }
    acces_token = create_access_token(data=token_data)
    return {"access_token": acces_token, "token_type": "bearer"}


@router.post("/activation")   # pour activer le compte et changer le mot de passe à la premiere connexion
def activation(password_form : NewPassword, db: db_dependency, current_user : Annotated[Users, Depends(get_current_user)]) : 
    """
    Active le compte d'un utilisateur et change son mot de passe lors de la première connexion.

    Args:
        password_form (NewPassword): Formulaire contenant le nouveau mot de passe et sa confirmation.
        db (Session): Session de base de données SQLAlchemy.
        current_user (Users): Utilisateur actuellement authentifié.

    Returns:
        dict: Message de confirmation d'activation du compte.

    Raises:
        HTTPException:
            - 404: Si l'utilisateur n'est pas trouvé
            - 400: Si le compte est déjà activé
            - 400: Si le mot de passe est manquant
            - 400: Si la confirmation est manquante
            - 400: Si les mots de passe ne correspondent pas

    Note:
        - Nécessite une authentification préalable
        - Le nouveau mot de passe est hashé avant stockage
        - Le statut is_active passe à 1 après activation
    """
    user = db.execute(text("select * from users where email = :email"), {"email" : current_user.email}).first()
    if not user : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé dans la base de données")
    if user.is_active :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Le compte est déjà activé")
    if not password_form.new_password :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Le mot de passe est obligatoire")
    if not password_form.confirm_password :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Veuliiez confirmer le mot de passe")
    if password_form.new_password != password_form.confirm_password :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Les mots de passe ne correspondent pas")
    
    hashed_password = get_password_hash(password_form.new_password)
    db.execute(text("update users set hashed_password = :hashed_password, is_active = 1 where email = :email"), {"hashed_password": hashed_password, "email": user.email})
    db.commit()
    return {"message": "Le compte a été activé avec succès"}

