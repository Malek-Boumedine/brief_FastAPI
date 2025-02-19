from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, Column, String



class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(sa_column=Column(String(255), unique=True))
    password: str = Field(sa_column=Column(String(255)))
    role: str = Field(sa_column=Column(String(50)), default="user")
    is_active: bool = Field(default=False)

class Loan_requests(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    statut: bool = Field(default=False)
    id_demandeur: int = Field(foreign_key="user.id")
    date_demande: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    
    
    
    
    
    
    
    