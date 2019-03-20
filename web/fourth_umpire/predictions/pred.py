import numpy as np
from sklearn.externals import joblib
import pickle
import os
from sklearn import metrics
import pandas as pd

import pandas_highcharts.core

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
    #frames = [cod_est, y_pruebas, y_pruebas_predict]
    #resultado = pd.DataFrame(pd.concat(frames,  axis=1))
    #resultado.columns = ["cod_est", "resultados_nuevos_reales", "resultados_nuevos_predecidos"]
    rel_path = "pre_pred/archivo_prueba_graficar.pkl"
    resultado = pd.read_pickle(os.path.join(script_dir, rel_path))
    resultado_predicc = resultado.loc[resultado['prediccion'] == 0]

    [chart_sexo, chart_edad, chart_procedencia, chart_tam_familia] = graficas(resultado_predicc)
    resultado_predicc = resultado_predicc[["cod_est","sex","age","address","famsize","prediccion"]]
    return valor_prediccion,resultado_predicc,chart_sexo,chart_edad,chart_procedencia,chart_tam_familia

#Grafica
def graficas(dataframe):
    sexo = pd.DataFrame(dataframe.groupby('sex')['cod_est'].nunique()).reset_index()
    edad = pd.DataFrame(dataframe.groupby('age')['cod_est'].nunique()).reset_index()
    procedencia = pd.DataFrame(dataframe.groupby('address')['cod_est'].nunique()).reset_index()
    tam_familia = pd.DataFrame(dataframe.groupby('famsize')['cod_est'].nunique()).reset_index()

    chart_sexo = pandas_highcharts.core.serialize(sexo, render_to='char_predict',
                                            output_type='json',
                                            kind = "bar",
                                            x ="sex",
                                            title="Distribucion general por sexo(Femenino-Masculino)"
                                            )
    chart_edad = pandas_highcharts.core.serialize(edad, render_to='chart_predict',
                                            output_type='json',
                                            kind = "bar",
                                            x ="age",
                                            title="Distribucion general por edad"
                                            )
    chart_procedencia = pandas_highcharts.core.serialize(procedencia, render_to='chart_predict',
                                            output_type='json',
                                            kind = "bar",
                                            x ="address",
                                            title="Distribucion general por procedencia(Urbano-Rural)"
                                            )
    chart_tam_familia = pandas_highcharts.core.serialize(tam_familia, render_to='chart_predict',
                                            output_type='json',
                                            kind = "bar",
                                            x ="famsize",
                                            title="Distribucion general por tamaño familiar(GT3-Mayor3, LE3-Menor3)"
                                            )


    return chart_sexo, chart_edad, chart_procedencia, chart_tam_familia

def get_carrera(id):
    teams = {
            '1':	'Ing. Electrónica',
            '2':	'Med. Veterinaria',
            '3':	'Ing. Eléctrica',
            '4':	'Ing. Sistemas',
            '5':	'Ing. Mecatrónica',
    }
    return teams[id]
