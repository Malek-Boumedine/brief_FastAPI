# Routes prêts
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import text
from typing import Annotated
from app.schemas import LoanRequest
from app.modeles import Users
from app.ml import predire, charger_modele
from app.utils import get_current_user, db_dependency
import pandas as pd
from datetime import datetime



router = APIRouter(prefix="/loans", tags=["loans"])  # pour les routes de prêts


@router.post("/request")  # pour demander un prêt
def demande_pret(user_data: LoanRequest, current_user: Annotated[str, Depends(get_current_user)], db: db_dependency) -> dict : 
    model = charger_modele()
    features = model.feature_names_
    data = pd.DataFrame([user_data.dict()], columns=features)
    prediction = predire(model, data)
    statut = int(prediction[0])
    
    db.execute(text("insert into loan_requests(statut, id_demandeur, date_demande) values (:statut, :id_demandeur, :date_demande)"), {"statut": statut, "id_demandeur": current_user.id_banque, "date_demande": datetime.now()})
    db.commit()
    
    # retourner si le pret est accordé ou non
    return {
        "résultat": "le prêt est accordé" if prediction[0] else "le prêt n'est pas accordé",
        "probabilité d'être accordé": float(model.predict_proba(data)[0][1])
        }


@router.get("/history")   # pour voir l'historique des demandes de prêts
def history(current_user: Annotated[Users, Depends(get_current_user)], db: db_dependency):
    role = current_user.role
    if role == "admin":
        liste_demandes = db.execute(text("select * from loan_requests")).mappings().all()
        return liste_demandes
    
    user_id = current_user.id_banque
    liste_demandes = db.execute(text("SELECT * FROM loan_requests WHERE id_demandeur = :user_id"),{"user_id": user_id}).mappings().all()
    return liste_demandes

