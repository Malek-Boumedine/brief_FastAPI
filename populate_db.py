from sqlmodel import Session, select
from faker import Faker
from datetime import datetime, timedelta
import random
from app.utils import bcrypt_context
from sqlmodel import SQLModel
from app.database import engine



from app.modeles import Users, Loan_requests
from app.database import engine


def populate_db():
    # Initialiser Faker
    fake = Faker()

    # Ouvrir une session SQLModel
    with Session(engine) as session:
        
        # Générer des utilisateurs fictifs
        users = []
        for _ in range(2):
            user = Users(
                nom_banque=fake.company(),
                email=fake.unique.email(),
                hashed_password=bcrypt_context.hash(fake.password(length=12)),
            )
            session.add(user)
            users.append(user)
        
        # Générer des demandes de prêt fictives
        for _ in range(5):
            loan_request = Loan_requests(
                statut=fake.boolean(chance_of_getting_true=50),  # 50% approuvé/refusé
                id_demandeur=random.randint(1000, 9999),
                date_demande=fake.date_time_between(start_date="-2y", end_date="now")  # Entre 2 ans et aujourd'hui
            )
            session.add(loan_request)

        session.commit()  # On commit pour enregistrer les demandes de prêt

    print("✅ Base de données remplie avec succès !")
    
if __name__ == "__main__" : 
    # remplir la BDD avec faker
    populate_db()

    # Créer les tables dans la base de données
    SQLModel.metadata.create_all(engine)

