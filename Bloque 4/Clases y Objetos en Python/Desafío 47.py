# Desafio Amplía la clase `Autor` para incluir una lista de libros escritos por el autor. Implementa métodos para agregar y eliminar libros de esta lista.

class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
