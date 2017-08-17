class Persona:

    __nombre = ""
    __edad = 0

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def es_mayor_edad(self):
        if self.__edad >= 18:
            return "MAYOR"
        else:
            return "MENOR"