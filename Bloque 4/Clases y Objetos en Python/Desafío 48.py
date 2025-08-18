# Declaramos la clase Autor
class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # Método para mostrar los datos del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

# Declaramos la clase Libro
class Libro:
    def __init__(self, titulo="", genero="", isbn="", autor=None):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor  # Relación directa con un objeto Autor

    # Método para mostrar los datos del libro
    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        if self.autor:
            print("Autor:")
            self.autor.mostrar_autor()
        else:
            print("Autor no asignado.")

# Creamos el objeto Autor y lo insertamos como atributo en el objeto Libro
autor1 = Autor("Mario Benedetti", "Uruguay")
libro1 = Libro("Gracias por el fuego", "Narrativa", "978-9875666372", autor1)

# Mostramos los datos del libro y su autor
libro1.mostrar_libro()
