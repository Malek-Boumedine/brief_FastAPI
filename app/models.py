# Modèles SQLModel (User, Loan)
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    password: str
    role: str = Field(default="user")
    is_active: bool = Field(default=False)


class loan_requests(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    statut: bool = Field(default=False)
    id_demandeur: int
    date_demande: datetime = Field(default_factory=datetime.utcnow, nullable=False)


    




