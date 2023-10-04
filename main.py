#Para importar las constraseñas de los usuarios
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth
#Librerías para la aplicación
import streamlit as st 
#Interacción con los datos
import pandas as pd
import numpy as pd
#Insertar el munú de navegación
from streamlit_option_menu import option_menu
#Modulo para cargar datos
import carga_datos as cd
#Interacción Base de datos
from con_firebase import FireBaseDB
from firebase_admin import db

path = ".gitignore\gestion-ovinos-firebase-adminsdk-v5u61-32dfae7bf3.json"
url = "https://gestion-ovinos-default-rtdb.firebaseio.com/"

fb_db = FireBaseDB(path,url)
#Configuraciones de la página
st.set_page_config(page_title="Gestion Ovinos", page_icon="🐑")


#--- User Authentication ---#
names = ['Rosmary Camacho', 'Ali Yarza', 'Ivan Cepeda']
usernames = ['rosmarycamacho', 'aliyarza', 'ivancepeda']
#Carga de passwords hasheados
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "gestion_ovinos", "abcdef")
name, authentication_status, username = authenticator.login("Login", "main")

#Mostrar mensaje, si el usuario tiene un error de usuario o contraseña
if authentication_status == False:
    st.error("Usuario o Contraseña incorrectos")
    
#Si hay un problema porque no se producido ninguna acción, mostrará
if authentication_status == None:
    st.warning("Por favor, ingrese un nombre de usuario y contraseña")

#Si todo está correcto, inicia la aplicación
if authentication_status == True:
    #crear menu superior
    

      
    #Mensaje Bienvanida al usuario
    st.success(name + "Este es tu espacio")
    #Boton de cierre de sesión
    authenticator.logout("Cerrar Sesión", "main")
    selected = option_menu(None, ["Nuevo Animal", "Procesos", "Dashboard", "Chat"],
        default_index = 0, 
        orientation = "horizontal"
        )
    selected
    #flujo interaccion del menu de carga de datos
    if selected == "Nuevo Animal":
        #Formulario de carga de datos animal
        with st.form(key="carga_datos_animal"):
            nombre = st.text_input ("Nombre_identificador")
            raza = st.text_input ("Raza")
            sexo = st.selectbox ("Sexo", ("Macho", "Hembra"))
            peso = st.text_input ("Peso")
            #imagen = st.file_uploader ('Añadir Imagen')
            nuevo_animal = st.form_submit_button ("Agregar Nuevo Animal")
            if nuevo_animal == True:
                dic_animales = cd.carga_animal(nombre, raza, sexo, peso)
                fb_db.escribir_registros("animales", dic_animales)
                res_animales = fb_db.leer_registros("animales")
                df_animales = cd.carga_dataframe(dic_animales) 
                st.write(df_animales)

    if selected == "Procesos":
            
            tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Proceso","Periodo", "Tratamiento", "Alimentación", "Plan Sanitario", "Rebaño", "Explotación", "Peso"])
            animal = []
            periodo = []
            tratamiento = []
            alimentacion = []
            plan_sanitario = []
            rebaño = []
            explotacion = []
            peso = []
            enfermedad = []

            with tab1:
                with st.form(key="carga_datos_procesos_animal"):
                    elegir_animal = st.selectbox ('Animal', animal)
                    elegir_periodo = st.selectbox ('periodo', periodo)
                    elegir_tratamiento = st.selectbox ('Tratamiento', tratamiento)
                    elegir_alimentacion = st.selectbox ('alimentacion', alimentacion)
                    elegir_plan_sanitario = st.selectbox ('plan_sanitario', plan_sanitario)
                    elegir_rebanio = st.selectbox ('rebaño', rebaño)
                    elegir_explotacion = st.selectbox ('explotacion', explotacion)
                    elegir_peso = st.selectbox ('peso', peso)
                    nuevo_proceso = st.form_submit_button ("Agregar Proceso")
                    if nuevo_proceso == True:
                        dic_procesos = cd.carga_proceso(elegir_animal, elegir_periodo, elegir_tratamiento, elegir_alimentacion, elegir_plan_sanitario, elegir_rebanio, elegir_explotacion, elegir_peso)
                        df_procesos = cd.carga_dataframe(dic_procesos) 
                        st.write(df_procesos)

            with tab2:
                with st.form(key="Cargar_Periodo"):
                    crear_periodo = st.text_input("Descripción Periodo")
                    fecha_inicio = st.date_input("Fecha Inicio", format="YYYY/MM/DD")
                    fecha_fin = st.date_input("Fecha Fin", format="YYYY/MM/DD")
                    nuevo_periodo = st.form_submit_button("Agregar Periodo")
                    if nuevo_periodo == True:
                        dic_periodos = cd.cargar_periodo(crear_periodo, fecha_inicio, fecha_fin)
                        df_periodos = cd.carga_dataframe(dic_periodos) 
                        st.write(df_periodos)
            with tab3:
                 with st.form(key="Cargar_Tratamiento"):
                    añadir_medico = st.text_input("Médico Tratante")
                    añadir_tratamiento = st.text_input("Elegir tratamiento")
                    elegir_enfermedad = st.selectbox("Elegir enfermedad", enfermedad)
                    añadir_famacha = st.text_input("Descripción Famacha")
                    añadir_condicion = st.text_input("Descripción Condición Corporal")
                    añadir_aborto = st.number_input("Cantidad de abortos")
                    nuevo_tratamiento = st.form_submit_button("Agregar Tratamiento")
                    if nuevo_tratamiento == True:
                        dic_tratamientos = cd.carga_tratamiento(añadir_medico, añadir_tratamiento, elegir_enfermedad, añadir_famacha, añadir_condicion, añadir_aborto)
                        df_tratamientos = cd.carga_dataframe(dic_tratamientos)
                        st.write(df_tratamientos)
            
            with tab4:
                 with st.form(key="Cargar_Alimentacion"):
                    crear_alimentacion = st.text_input("Tipo de Alimentación")
                    crear_suplemento = st.text_input("Tipo de Suplemento")
                    nuevo_alimentacion = st.form_submit_button("Agregar Alimentación")
                    if nuevo_alimentacion == True:
                        dic_alimentacion = cd.carga_alimentacion(crear_alimentacion, crear_suplemento)
                        df_alimentacion = cd.carga_dataframe(dic_alimentacion)
                        st.write(df_alimentacion)
            
            with tab5:
                with st.form(key="Cargar_Plan_Sanitario"):
                    crear_desparacitacion = st.text_input("Desparacitación")
                    crear_vacunacion = st.text_input("Vacunación")
                    nuevo_plan_sanitario = st.form_submit_button("Agregar Plan Sanitario")
                    if nuevo_plan_sanitario == True:
                        dic_plan_sanitario = cd.cargar_plan_sanitario(crear_desparacitacion, crear_vacunacion)
                        df_plan_sanitario = cd.carga_dataframe(dic_plan_sanitario)
                        st.write(df_plan_sanitario)
            
            with tab6:
                with st.form(key="Cargar_Rebaño"):
                    crear_rebanio = st.text_input("Rebaño")
                    nuevo_rebanioo = st.form_submit_button("Agregar Rebaño")
                    if nuevo_rebanioo == True:
                        dic_rebanio = cd.carga_rebaño(crear_rebanio)
                        df_rebanio = cd.carga_dataframe(dic_rebanio)
                        st.write(df_rebanio)
            with tab7:
                with st.form(key="Cargar_Explotación"):
                    crear_explotacion = st.text_input("Explotación")
                    nuevo_explotacion = st.form_submit_button("Agregar Explotación")
                    if nuevo_explotacion == True:
                        dic_explotacion = cd.carga_explotacion(crear_explotacion)
                        df_explotacion = cd.carga_dataframe(dic_explotacion)
                        st.write(df_explotacion)    
            with tab8:
                with st.form(key="Cargar_Peso"):
                    crear_peso = st.text_input("Peso")
                    nuevo_peso = st.form_submit_button("Agregar Peso")
                    if nuevo_peso == True:
                        dic_peso = cd.carga_peso(crear_peso)
                        df_peso = cd.carga_dataframe(dic_peso)
                        st.write(df_peso)

    if selected == "Dashboard":
        st.markdown("En Construcción")
    if selected == "Chat":
        st.markdown("En Construcción")


    
    
