# Routes prêts
from fastapi import FastAPI, Depends
from .database import db_connection
from sqlmodel import text

app = FastAPI()




@app.post("loans/request") 
def demande_pret(): 
    # importer le modele de prédiction
    # importer les données de l'utilisateur
    # prédire le prêt
    # se connecter a la base de données
    # enregistrer la prediction dans la base de données
    # retourner si le pret est accordé ou non
    
    return {"message": "Demande de prêt accordée ou pas"}



@app.get("/loans/history")
def history(connexion = Depends(db_connection)):
    liste_demandes = connexion.execute(text("select * from loan_requests"))
    return liste_demandes.fetchall() 




@app.get("/")
def test():
    return {"message" : "bienvenue sur mon api"}


