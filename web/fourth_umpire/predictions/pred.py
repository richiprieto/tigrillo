import numpy as np
from sklearn.externals import joblib
import pickle
import os
from sklearn import metrics

script_dir = os.path.dirname(__file__)

#falta agregar las predicciones correctas
def pre_match_predict(season,team1,team2,city):
    rel_path = "pre_pred/entrenamiento_general.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    modelo_entrenado = joblib.load(abs_file_path)

    rel_path = "pre_pred/X_test_general.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    X_test = pickle.load( open( abs_file_path, "rb" ))

    rel_path = "pre_pred/y_test_general.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    y_test = pickle.load( open( abs_file_path, "rb" ))

    y_pred = modelo_entrenado.predict(X_test)

    return metrics.accuracy_score(y_test, y_pred)
