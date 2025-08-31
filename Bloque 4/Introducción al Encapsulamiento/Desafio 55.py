class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    # Get y set para nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Get y set para nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    # Método para agregar libros
    def agregar_libro(self, titulo_libro):
        self.__libros.append(titulo_libro)

    # Método para obtener la lista de libros (sin exponerla directamente)
    def get_libros(self):
        return list(self.__libros)  # Devuelve una copia para proteger la lista original

    # Método para mostrar información del autor
    def mostrar_info(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")
        print("Libros:")
        if self.__libros:
            for libro in self.__libros:
                print(f" - {libro}")
        else:
            print(" - Sin libros registrados")

# Función externa que accede a los libros del autor de forma segura
def obtener_titulos(autor):
    return autor.get_libros()

# Ejemplo de uso
if __name__ == "__main__":
    autor1 = Autor("Eduardo Galeano", "Uruguaya")
    autor1.agregar_libro("Las venas abiertas de América Latina")
    autor1.agregar_libro("El libro de los abrazos")
    autor1.agregar_libro("Patas arriba: La escuela del mundo al revés")

    autor1.mostrar_info()

    # Usar la función externa para obtener títulos
    titulos = obtener_titulos(autor1)
    print("\nTítulos obtenidos desde función externa:")
    for titulo in titulos:
        print(" *", titulo)
