# Routes auth
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Union
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from modeles import User
from database import db_connection


# database = db_connection()
database = "sqlite:///./test.db"

class Token(BaseModel) : 
    acces_token : str
    token_type : str

class TokenData(BaseModel) :
    username : Union[str, None]
    
class UserDB(User) : 
    hashed_password : str
    

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()



def verify_password(password : str, hashed_password : str) -> str: 
    return pwd_context.verify(password, hashed_password)

def get_password_hash(password : str) -> str: 
    return pwd_context.hash(password)


@app.get("/test")
async def test() -> dict :
    return {"message" : "hello world"}



@app.post("/auth/login")
def login() :
    pass





@app.post("/auth/activation")
def activation() :
    pass




@app.post("/auth/logout")
def logout() : 
    pass



