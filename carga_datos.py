import pandas as pd
import streamlit as st

def get_session_state(username, usernames):
    if username == usernames[0]:
        session = st.session_state[username]
    elif username == usernames[1]:
        session = st.session_state[username]
    elif username == usernames[2]:
        session = st.session_state[username]
    return session

"""permitirá la carga de los datos"""
def carga_animal(nombre, raza, sexo, peso):
    animal = {'Nombre_animal':nombre, 'raza':raza, 'sexo':sexo, 'peso':peso}
    return animal

def carga_proceso(elegir_animal, elegir_periodo, elegir_tratamiento, elegir_alimentacion, elegir_plan_sanitario, elegir_rebanio, elegir_explotacion, elegir_peso):
    proceso = {'Animal':elegir_animal, 'Periodo':elegir_periodo, 'Tratamiento':elegir_tratamiento, 'Alimentación':elegir_alimentacion, 'Plan Sanitario':elegir_plan_sanitario, 'Rebaño':elegir_rebanio, 'Explotación':elegir_explotacion, 'Peso':elegir_peso}
    return proceso

def cargar_periodo (crear_periodo, fecha_inicio, fecha_fin):
    periodo = {'Descripción Periodo':crear_periodo, 'Fecha Inicio':fecha_inicio, 'Fecha Fin':fecha_fin}
    return periodo

def carga_tratamiento(añadir_medico, añadir_tratamiento, elegir_enfermedad, añadir_famacha, añadir_condicion, añadir_aborto):
    tratamiento = {'Médico Tratante':añadir_medico, 'Descripción Tratamiento':añadir_tratamiento, 'Elegir enfermedad':elegir_enfermedad, 'Descripción Famacha':añadir_famacha, 'Descripción Condición Corporal':añadir_condicion, 'Cantidad de abortos':añadir_aborto}
    return tratamiento 

def carga_alimentacion(crear_alimentacion, crear_suplemento):
    alimentacion = {'Tipo de Alimentación':crear_alimentacion, 'Tipo de Suplemento':crear_suplemento}
    return alimentacion

def cargar_plan_sanitario(crear_desparacitacion, crear_vacunacion):
    plan_sanitario = {'Desparacitación':crear_desparacitacion, 'Vacunación':crear_vacunacion}
    return plan_sanitario

def carga_rebaño(crear_rebanio):
    rebanio = {'Rebaño':crear_rebanio}
    return rebanio

def carga_explotacion(crear_explotacion):
    explotacion = {'Explotación':crear_explotacion}
    return explotacion

def carga_peso(crear_peso):
    peso = {'Peso':crear_peso}
    return peso

def carga_enfermedad(elegir_enfermedad):
    enfermedad = {'Elegir enfermedad':elegir_enfermedad}
    return enfermedad


#Datos cargados a un dataframe
def carga_dataframe(diccionario):
    #convertir diccionario a un dataframe
    dataFrame = pd.DataFrame(diccionario, index=[0])
    return dataFrame

"""Carga los datos a un dataframe"""
"""# Crear un dataframe de ejemplo
df = pd.DataFrame({'columna1': [1, 2, 3], 'columna2': ['a', 'b', 'c']})

# Crear una nueva fila con los datos que desea agregar
nueva_fila = pd.DataFrame({'columna1': [4], 'columna2': ['d']})

# Verificar si los datos ya existen en el dataframe
if not nueva_fila.isin(df).all().all():
    # Agregar la nueva fila al dataframe
    df = df.append(nueva_fila, ignore_index=True)"""

if __name__=='__main__':
    carga_animal()
    carga_dataframe()



