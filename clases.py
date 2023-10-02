import pandas as pd

class CargaDatos:
    """permitirá la carga de los datos"""
    def carga_animal(self, nombre, raza, sexo, peso):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.peso = peso
        animal = {'Nombre_animal':nombre, 'raza':raza, 'sexo':sexo, 'peso':peso}

    def carga_proceso(self, elegir_animal, elegir_periodo, elegir_alimentacion, elegir_plan_sanitario, elegir_rebanio, elegir_explotacion, elegir_peso):
        self.elegir_animal = elegir_animal
        self.elegir_periodo = elegir_periodo
        self.elegir_plan_sanitario = elegir_plan_sanitario
        self.elegir_rebanio = 

    #Datos cargados a un dataframe
    def carga_dataframe(self, df):
        dataFrame = df
        return dataFrame
    


