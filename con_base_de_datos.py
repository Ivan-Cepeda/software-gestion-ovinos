import sqlite3

#Creamos la conexión con la base de datos
conn = sqlite3.connect('ovinos.db')
#Creamos el cursor para ejecutae las queries


def crear_tablas(conn):
    c = conn.cursor()
    #Creamos la tabla Enfermedad
    c.execute(""" CREATE TABLE IF NOT EXISTS alimentacion (
                idAlimentacion INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                suplemento TEXT NOT NULL);""")


    #Creamos la tabla Enfermedad
    c.execute(""" CREATE TABLE IF NOT EXISTS enfermedad (
            idEnfermedad INTEGER PRIMARY KEY AUTOINCREMENT,
            enfermedad TEXT NOT NULL          
            );""")


    #Creamos la tabla Tratamiento
    c.execute(""" CREATE TABLE IF NOT EXISTS tratamiento (
            idTratamiento INTEGER PRIMARY KEY AUTOINCREMENT,
            idEnfermedad INTEGER,
            medico TEXT NOT NULL,
            famacha TEXT NOT NULL,
            condicion_corporal TEXT NOT NULL,
            aborto NUMERIC NOT NULL,
            FOREIGN KEY (idEnfermedad) REFERENCES enfermedad(idEnfermedad)
            );""")


    #Creamos la tabla Explotacion
    c.execute(""" CREATE TABLE IF NOT EXISTS explotacion (
            idExplotacion INTEGER PRIMARY KEY AUTOINCREMENT,
            tipoExplotacion TEXT NOT NULL
            );""")


    #Creamos la tabla Rebaño
    c.execute(""" CREATE TABLE IF NOT EXISTS rebaño (
            idRebaño INTEGER PRIMARY KEY AUTOINCREMENT,
            rebaño TEXT NOT NULL
            );""")


    #Creamos la tabla Peso
    c.execute(""" CREATE TABLE IF NOT EXISTS control_peso (
            idPeso INTEGER PRIMARY KEY AUTOINCREMENT,
            Peso NUMERIC NOT NULL
            );""")


    #creamos la tabla Plan Sanitario
    c.execute(""" CREATE TABLE IF NOT EXISTS Plan Sanitario (
            idPlanSanitario INTEGER PRIMARY KEY AUTOINCREMENT,
            desparacitacion TEXT NOT NULL,
            vacunacion TEXT NOT NULL
            );""")


    #Tabla Imagen
    c.execute(""" CREATE TABLE IF NOT EXISTS imagen (
            idImagen INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL
            );""")


    #Tabla Animal
    c.execute(""" CREATE TABLE IF NOT EXISTS animal (
            idAnimal INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            raza TEXT NOT NULL,
            pesoNacimiento NUMERIC NOT NULL,
            Vivo TEXT NOT NULL,
            idImagen INTEGER
            FOREIGN KEY (idImagen) REFERENCES imagen(idImagen)
            );""")


    #Crear la tabla periodo las fechas formato YYYY-MM-DD, HH:MM:SS
    c.execute(""" CREATE TABLE IF NOT EXISTS periodo (
            idPeriodo INTEGER PRIMARY KEY AUTOINCREMENT,
            periodo TEXT NOT NULL
            fechaInicio DATE NOT NULL,
            fechaFin TEXT NOT NULL
            );""")


    #Crear la tabla usuario
    c.execute(""" CREATE TABLE IF NOT EXISTS usuario (
            idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            correo TEXT NOT NULL,
            contraseña TEXT NOT NULL
            );""")


    #Crear la tabla procesos
    c.execute(""" CREATE TABLE IF NOT EXISTS proceso (
            idProceso INTEGER PRIMARY KEY AUTOINCREMENT,
            idPeriodo INTEGER,
            idAnimal INTEGER,
            idAlimentacion INTEGER,
            idTratamiento INTEGER,
            idExplotacion INTEGER,
            idRebaño INTEGER,
            idPeso INTEGER,
            idPlanSanitario INTEGER,
            idUsuario INTEGER,
            FOREIGN KEY (idPeriodo) REFERENCES periodo(idPeriodo),
            FOREIGN KEY (idAnimal) REFERENCES animal(idAnimal),
            FOREIGN KEY (idAlimentacion) REFERENCES alimentacion(idAlimentacion),
            FOREIGN KEY (idTratamiento) REFERENCES tratamiento(idTratamiento),
            FOREIGN KEY (idExplotacion) REFERENCES explotacion(idExplotacion),
            FOREIGN KEY (idRebaño) REFERENCES rebaño(idRebaño),
            FOREIGN KEY (idPeso) REFERENCES control_peso(idPeso),
            FOREIGN KEY (idPlanSanitario) REFERENCES Plan Sanitario(idPlanSanitario),
            FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario) 
            );""")


    conn.commit()
    c.conn.close()

def cargar_usuario(conn):
    c = conn.cursor()
    c.execute(""" SELECT * FROM usuario;""")
    return c.fetchall()



if __name__ == '__main__':
    crear_tablas(conn)
    cargar_usuario(conn)