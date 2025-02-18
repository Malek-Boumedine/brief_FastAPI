# Routes auth
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer



app = FastAPI()

# Déclare l'URL où le client obtiendra le token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@app.post("/auth/login")
def login() :
    pass





@app.post("/auth/activation")
def activation() :
    pass




@app.post("/auth/logout")
def logout() : 
    pass



