# Point d'entrée de l'application
from fastapi import FastAPI
from app.endpoints import route_loans, route_admin, route_auth



# Créer l'application FastAPI
app = FastAPI(title="API de prêts", description="API pour prédire l'accord de prêts", version="0.1")

# inclure les routes
app.include_router(route_loans.router)
app.include_router(route_admin.router)
app.include_router(route_auth.router)

# route racine
# @app.get("/")
# def read_root():
#     return {"message": "API gestion de prêts"}


