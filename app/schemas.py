# Schémas Pydantic
# Dans un nouveau fichier schemas.py
from pydantic import BaseModel, Field, EmailStr
from app.modeles import Users
from typing import Union

class LoanRequest(BaseModel):
    City: str = Field(..., description="Ville")
    State: str = Field(..., description="État", max_length=2)
    Zip: int = Field(..., description="Code postal")
    Bank: str = Field(..., description="Nom de la banque")
    BankState: str = Field(..., description="État de la banque", max_length=2)
    NAICS: int = Field(..., description="Code NAICS")
    ApprovalFY: int = Field(..., description="Année fiscale d'approbation")
    Term: int = Field(..., description="Durée du prêt en mois")
    NoEmp: int = Field(..., description="Nombre d'employés")
    NewExist: float = Field(..., description="Nouvelle entreprise ou existante")  # Changed to float
    CreateJob: int = Field(..., description="Nombre d'emplois créés")
    RetainedJob: int = Field(..., description="Nombre d'emplois conservés")
    FranchiseCode: int = Field(..., description="Code franchise")
    UrbanRural: int = Field(..., description="Zone urbaine (1) ou rurale (0)")
    LowDoc: int = Field(..., description="Programme LowDoc (1) ou non (0)")
    DisbursementGross: float = Field(..., description="Montant brut distribué")  # Moved up
    GrAppv: float = Field(..., description="Montant brut approuvé")  # Moved up
    RevLineCr: int = Field(..., description="Ligne de crédit renouvelable")  # Changed to int

    class Config:
        json_schema_extra = {
            "example": {
                "City": "SPRINGFIELD",
                "State": "TN",
                "Zip": 37172,
                "Bank": "BBCN BANK",
                "BankState": "CA",
                "NAICS": 453110,
                "ApprovalFY": 2008,
                "Term": 6,
                "NoEmp": 4,
                "NewExist": 1.0,
                "CreateJob": 2,
                "RetainedJob": 250,
                "FranchiseCode": 1,
                "UrbanRural": 1,
                "LowDoc": 0,
                "DisbursementGross": 20000.0,
                "GrAppv": 20000.0,
                "RevLineCr": 0
            }
        }        


class CreateUserRequest(BaseModel):
    nom_banque: str = Field(..., description="Nom de la banque")
    email: EmailStr
    password: str = Field(..., min_length=8, description="longueur minimale de 8 caractères")
    
    class Config:
        json_schema_extra = {
            "example": {
                "nom_banque": "Bank 1",
                "email": "mon_email@domaine.com",
                "password": "azerty12",
            }
        }        

class Token(BaseModel) : 
    acces_token : str
    token_type : str


class TokenData(BaseModel) :
    username : Union[str, None]
    

class UserDB(Users) : 
    pass


