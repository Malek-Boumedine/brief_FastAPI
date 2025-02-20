# Modèle prédiction
import pickle
import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import FunctionTransformer



def transform_naics(X):
    return X['NAICS'].astype(str).str[:2].astype(int).values.reshape(-1, 1)

def transform_franchise(X):
    return X['FranchiseCode'].apply(lambda x: 1 if x in [0, 1] else 0).values.reshape(-1, 1)

def charger_modele(fichier_pkl : str ="best_cat_boost.pkl") -> "model":
    with open(fichier_pkl, 'rb') as f:
        return pickle.load(f)

def predire(model : "model", donnees : pd.DataFrame) -> int: 
    return model.predict(donnees)


# modele sans pipeline  
# model = charger_modele()

# modele avec pipeline
# model = charger_modele("cat_boost_pileline.pkl")


if __name__ == "__main__":
    model = charger_modele("best_cat_boost.pkl")
    features = model.feature_names_
    # features = ['City', 'State', 'Zip', 'Bank', 'BankState', 'NAICS', 'ApprovalFY', 'Term', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'FranchiseCode', 'UrbanRural', 'LowDoc', 'DisbursementGross', 'GrAppv', 'RevLineCr']
    test = ["SPRINGFIELD", "TN", 37172, "BBCN BANK", "CA", 453110, 2008, 6, 4, 1.0, 2, 250, 1, 1, 0, 20000.0, 20000.0, 0] 
    # test_df = pd.DataFrame([test], columns=features)
    test_df = test

    prediciton = model.predict(test)
    print("va payer" if prediciton else "ne va pas payer")
    print(prediciton)
    print(model.predict_proba(test_df))
    print(list(features))
    print(model.get_cat_feature_indices())



