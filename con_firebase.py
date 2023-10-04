import firebase_admin
from firebase_admin import credentials, db




class FireBaseDB:
    def __init__(self, credencial_path, database_url):
        #Inicializar credenciales de firebase
        cred = credentials.Certificate(credencial_path)
        firebase_admin.initialize_app(cred)

    def escribir_registros(self, path, data):
        # Escribir datos para las especificaciones de firebase
        ref = db.reference(path)
        ref.set(data)

    def leer_registros(self, path):
        # Leer datos para las especificaciones de firebase
        ref = db.reference(path)
        return ref.get()
    
    def borrar_registros(self, path):
        # Borrar datos para las especificaciones de firebase
        ref = db.reference(path)
        ref.delete()

    def actualizar_registros(self, path, data):
        # Actualizar datos para las especificaciones de firebase
        ref = db.reference(path)
        ref.update(data)
        