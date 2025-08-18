# Clase Autor: representa a un autor literario con nombre y nacionalidad

class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # Muestra los datos del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")


# Clase Libro: representa un libro con título, género, ISBN y su autor
class Libro:
    def __init__(self, titulo="", genero="", isbn="", autor=None):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor  # Relación directa con un objeto Autor

    # Muestra los datos del libro y del autor si está asignado
    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        if self.autor:
            print("Autor:")
            self.autor.mostrar_autor()
        else:
            print("Autor no asignado.")


# Clase Biblioteca: almacena múltiples autores y libros
class Biblioteca:
    def __init__(self):
        self.autores = []  # Lista de objetos Autor
        self.libros = []   # Lista de objetos Libro

    # Agrega un autor a la biblioteca
    def agregar_autor(self, autor):
        self.autores.append(autor)

    # Agrega un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Muestra todos los libros registrados
    def mostrar_todos_los_libros(self):
        print("\nListado de libros en la biblioteca:")
        for libro in self.libros:
            libro.mostrar_libro()
            print("-" * 30)

    # Muestra todos los autores registrados
    def mostrar_todos_los_autores(self):
        print("\nListado de autores en la biblioteca:")
        for autor in self.autores:
            autor.mostrar_autor()
            print("-" * 30)


# Ejemplo de uso del sistema de biblioteca

# Creamos autores
autor1 = Autor("Mario Benedetti", "Uruguay")
autor2 = Autor("Isabel Allende", "Chile")

# Creamos libros y los asociamos con autores
libro1 = Libro("Gracias por el fuego", "Narrativa", "978-9875666372", autor1)
libro2 = Libro("La casa de los espíritus", "Novela", "978-0060883287", autor2)

# Creamos la biblioteca y agregamos autores y libros
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_autor(autor1)
mi_biblioteca.agregar_autor(autor2)
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Mostramos la información almacenada
mi_biblioteca.mostrar_todos_los_autores()
mi_biblioteca.mostrar_todos_los_libros()


