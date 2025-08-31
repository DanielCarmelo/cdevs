class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    # Get para nombre
    @property
    def nombre(self):
        return self.__nombre

    # Set para nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Get para nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Set para nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad
