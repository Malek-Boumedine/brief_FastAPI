# Routes prêts
from fastapi import FastAPI
from database import db_connection


app = FastAPI()




@app.post("loans/request") 
def demande_pret(): 
    # importer le modele de prédiction
    # importer les données de l'utilisateur
    # prédire le prêt
    # enregistrer la prediction dans la base de données
    # retourner si le pret est accordé ou non
    
    return {"message": "Demande de prêt accordée ou pas"}




@app.get("/loans/history")
def history():
    return {"message": "Historique des prêts"}





