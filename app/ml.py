# Modèle prédiction
import cloudpickle
import pandas as pd



def charger_modele(fichier_pkl : str ="cat_boost_pileline.pkl") -> "model":
    with open(fichier_pkl, 'rb') as f:
        return cloudpickle.load(f)

def predire(model, donnees) : 
    return model.predict(donnees)

def transform_naics(X):
    return X['NAICS'].astype(str).str[:2].astype(int).values.reshape(-1, 1)

def transform_franchise(X):
    return X['FranchiseCode'].apply(lambda x: 1 if x in [0, 1] else 0).values.reshape(-1, 1)

# modele sans pipeline  
# model = charger_modele("best_cat_boost.pkl")

# modele avec pipeline
model = charger_modele()

# features = ['City', 'State', 'Zip', 'Bank', 'BankState', 'NAICS', 'ApprovalFY', 'Term', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'FranchiseCode', 'UrbanRural', 'LowDoc', 'DisbursementGross', 'GrAppv', 'RevLineCr']
features = model.feature_names_in_
test = ["SPRINGFIELD", "TN", 37172, "BBCN BANK", "CA", 453110, 2006, 84, 4, 1.0, 2, 250, 1, 1, 0, "20000.0", "20000.0", 0] 
test_df = pd.DataFrame([test], columns=features)

prediciton = model.predict(test_df)
print("va payer" if prediciton[0] else "ne va pas payer")
print(prediciton)



