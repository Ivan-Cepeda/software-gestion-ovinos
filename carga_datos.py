import pandas as pd

class CargaDatos:
    """permitirá la carga de los datos"""
    def carga_animal(self, nombre, raza, sexo, peso):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.peso = peso
        animal = {'Nombre_animal':nombre, 'raza':raza, 'sexo':sexo, 'peso':peso}
        return animal
    def carga_proceso(self, elegir_animal, elegir_periodo, elegir_tratamiento, elegir_alimentacion, elegir_plan_sanitario, elegir_rebanio, elegir_explotacion, elegir_peso):
        self.elegir_animal = elegir_animal
        self.elegir_periodo = elegir_periodo
        self.elegir_tratamiento = elegir_tratamiento
        self.elegir_alimentacion = elegir_alimentacion
        self.elegir_plan_sanitario = elegir_plan_sanitario
        self.elegir_rebanio = elegir_rebanio
        self.elegir_explotacion = elegir_explotacion
        self.elegir_peso = elegir_peso
        proceso = {'Animal':elegir_animal, 'Periodo':elegir_periodo, 'Tratamiento':elegir_tratamiento, 'Alimentación':elegir_alimentacion, 'Plan Sanitario':elegir_plan_sanitario, 'Rebaño':elegir_rebanio, 'Explotación':elegir_explotacion, 'Peso':elegir_peso }
        return proceso
    
   

   
    
    #Datos cargados a un dataframe
    def carga_dataframe(self, diccionario):
        #convertir diccionario a un dataframe
        dataFrame = pd.DataFrame(diccionario)
        return dataFrame
    



