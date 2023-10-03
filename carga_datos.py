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
    animal = pd.DataFrame({'Nombre_animal':nombre, 'raza':raza, 'sexo':sexo, 'peso':peso}, index=[0])
    return animal
def carga_proceso(elegir_animal, elegir_periodo, elegir_tratamiento, elegir_alimentacion, elegir_plan_sanitario, elegir_rebanio, elegir_explotacion, elegir_peso):
    proceso = {'Animal':elegir_animal, 'Periodo':elegir_periodo, 'Tratamiento':elegir_tratamiento, 'Alimentación':elegir_alimentacion, 'Plan Sanitario':elegir_plan_sanitario, 'Rebaño':elegir_rebanio, 'Explotación':elegir_explotacion, 'Peso':elegir_peso }
    return proceso




#Datos cargados a un dataframe
def carga_dataframe(diccionario):
    #convertir diccionario a un dataframe
    dataFrame = pd.DataFrame(diccionario)
    return dataFrame

if __name__=='__main__':
    carga_animal()
    carga_dataframe()



