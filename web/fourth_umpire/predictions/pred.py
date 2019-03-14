import numpy as np
from sklearn.externals import joblib
import pickle
import os
from sklearn import metrics
import pandas as pd

script_dir = os.path.dirname(__file__)

#falta agregar las predicciones correctas
def pre_match_predict(document):
    rel_path = "pre_pred/entrenamiento_general_kneighbors_80.0inicio.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    entrenamiento = joblib.load(abs_file_path)

    rel_path = document
    abs_file_path = os.path.join(script_dir, rel_path)
    archivo = pd.read_csv(abs_file_path)

    cod_est = archivo.cod_est
    y_pruebas = archivo.aprueba
    x_pruebas = archivo.iloc[:,1:30]
    y_pruebas_predict = pd.Series(entrenamiento.predict(x_pruebas))
    valor_prediccion = metrics.accuracy_score(y_pruebas, y_pruebas_predict)*100
    frames = [cod_est, y_pruebas, y_pruebas_predict]
    resultado = pd.DataFrame(pd.concat(frames,  axis=1))
    resultado.columns = ["cod_est", "resultados_nuevos_reales", "resultados_nuevos_predecidos"]
    sexo = graficas(archivo)
    return valor_prediccion,resultado,sexo

def graficas(archivo):
    sexo = pd.DataFrame(archivo.groupby('sex')['cod_est'].nunique()).reset_index()
    transforma = pd.Series(np.where(sexo.sex.values == 0, "Femenino", "Masculino"),
          sexo.index)
    sexo.sex = transforma
    sexo = sexo.rename(columns = {'cod_est':'Sexo'})

    return sexo

def get_carrera(id):
    teams = {
            '1':	'Ing. Electrónica',
            '2':	'Med. Veterinaria',
            '3':	'Ing. Eléctrica',
            '4':	'Ing. Sistemas',
            '5':	'Ing. Mecatrónica',
    }
    return teams[id]
