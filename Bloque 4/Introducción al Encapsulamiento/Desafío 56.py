class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

    def agregar_libro(self, titulo_libro):
        self.__libros.append(titulo_libro)

    def get_libros(self):
        return list(self.__libros)

    def mostrar_info(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")
        print("Libros publicados:")
        if self.__libros:
            for libro in self.__libros:
                print(f" - {libro}")
        else:
            print(" - Sin libros registrados")

# Función para encontrar el autor con más libros
def autor_con_mas_libros(lista_autores):
    if not lista_autores:
        return None

    max_autor = lista_autores[0]
    max_libros = len(max_autor.get_libros())

    for autor in lista_autores[1:]:
        cantidad = len(autor.get_libros())
        if cantidad > max_libros:
            max_autor = autor
            max_libros = cantidad

    return max_autor

#  Ejemplo *******************************************************************************
if __name__ == "__main__":
    autor1 = Autor("Mario Benedetti", "Uruguaya")
    autor1.agregar_libro("La tregua")
    autor1.agregar_libro("Gracias por el fuego")
    autor1.agregar_libro("Primavera con una esquina rota")
    autor1.agregar_libro("El cumpleaños de Juan Ángel")

    autor2 = Autor("Idea Vilariño", "Uruguaya")
    autor2.agregar_libro("Poemas de amor")
    autor2.agregar_libro("No")

    autor3 = Autor("Eduardo Galeano", "Uruguaya")
    autor3.agregar_libro("Las venas abiertas de América Latina")
    autor3.agregar_libro("El libro de los abrazos")
    autor3.agregar_libro("Patas arriba: La escuela del mundo al revés")

    autores = [autor1, autor2, autor3]
    autor_destacado = autor_con_mas_libros(autores)

    print("\nAutor uruguayo con más libros registrados:")
    autor_destacado.mostrar_info()
