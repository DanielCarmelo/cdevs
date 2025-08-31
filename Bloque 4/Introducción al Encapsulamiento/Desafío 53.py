class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista para almacenar títulos de libros

    # Getters y setters básicos
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para agregar un libro a la lista
    def agregar_libro(self, titulo_libro):
        self.__libros.append(titulo_libro)

    # Método para obtener la lista de libros
    def get_libros(self):
        return self.__libros

    # Método para mostrar toda la información del autor 
    def mostrar_info(self):
        print(f"Autor: {self.__nombre} ({self.__nacionalidad})")
        print("Libros:")
        if self.__libros:
            for libro in self.__libros:
                print(f" - {libro}")
        else:
            print(" - Sin libros registrados")

# Ejemplo de uso
if __name__ == "__main__":
    autor1 = Autor("Eduardo Galeano", "Uruguaya")
    autor1.agregar_libro("Las venas abiertas de América Latina")
    autor1.agregar_libro("El libro de los abrazos")
    autor1.agregar_libro("Patas arriba: La escuela del mundo al revés")

    autor1.mostrar_info()
