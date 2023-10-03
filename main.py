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
                df_animales = cd.carga_animal(nombre, raza, sexo, peso)
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
            with tab2:
                with st.form(key="Cargar_Periodo"):
                    crear_periodo = st.text_input("Descripción Periodo")
                    fecha_inicio = st.date_input("Fecha Inicio", format="YYYY/MM/DD")
                    fecha_fin = st.date_input("Fecha Fin", format="YYYY/MM/DD")
                    nuevo_periodo = st.form_submit_button("Agregar Periodo")
            
            with tab3:
                 with st.form(key="Cargar_Tratamiento"):
                    añadir_medico = st.text_input("Descripción Tratamiento")
                    elegir_enfermedad = st.selectbox("Elegir enfermedad", enfermedad)
                    añadir_famacha = st.text_input("Descripción Famacha")
                    añadir_condicion = st.text_input("Descripción Condición Corporal")
                    añadir_aborto = st.number_input("Cantidad de abortos")
                    nuevo_tratamiento = st.form_submit_button("Agregar Tratamiento")
            
            with tab4:
                 with st.form(key="Cargar_Alimentacion"):
                    crear_alimentacion = st.text_input("Tipo de Alimentación")
                    crear_suplemento = st.text_input("Tipo de Suplemento")
                    nuevo_alimentacion = st.form_submit_button("Agregar Alimentación")
            
            with tab5:
                with st.form(key="Cargar_Plan_Sanitario"):
                    crear_desparacitacion = st.text_input("Desparacitación")
                    crear_vacunacion = st.text_input("Vacunación")
                    nuevo_plan_sanitario = st.form_submit_button("Agregar Plan Sanitario")
            
            with tab6:
                with st.form(key="Cargar_Rebaño"):
                    crear_rebaño = st.text_input("Rebaño")
                    nuevo_rebaño = st.form_submit_button("Agregar Rebaño")
            
            with tab7:
                with st.form(key="Cargar_Explotación"):
                    crear_explotacion = st.text_input("Explotación")
                    nuevo_explotacion = st.form_submit_button("Agregar Explotación")
            
            with tab8:
                with st.form(key="Cargar_Peso"):
                    crear_peso = st.text_input("Peso")
                    nuevo_peso = st.form_submit_button("Agregar Peso")
            
    if selected == "Dashboard":
        st.markdown("En Construcción")
    if selected == "Chat":
        st.markdown("En Construcción")
    
    
