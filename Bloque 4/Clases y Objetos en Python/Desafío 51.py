# Clase Autor
class Autor:
    def __init__(self, nombre="", nacionalidad="", fecha_nacimiento="", formacion=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.formacion = formacion

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Formación académica: {self.formacion}")

    def editar_autor(self, nombre=None, nacionalidad=None, fecha_nacimiento=None, formacion=None):
        if nombre: self.nombre = nombre
        if nacionalidad: self.nacionalidad = nacionalidad
        if fecha_nacimiento: self.fecha_nacimiento = fecha_nacimiento
        if formacion: self.formacion = formacion


# Clase Libro
class Libro:
    def __init__(self, titulo="", genero="", isbn="", autor=None):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        if self.autor:
            print("Autor:")
            self.autor.mostrar_autor()
        else:
            print("Autor no asignado.")


# Clase Biblioteca con funciones de búsqueda
class Biblioteca:
    def __init__(self):
        self.autores = []
        self.libros = []

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_autor_por_nombre(self, nombre):
        encontrados = [autor for autor in self.autores if nombre.lower() in autor.nombre.lower()]
        if encontrados:
            print("\nAutores encontrados:")
            for autor in encontrados:
                autor.mostrar_autor()
                print("-" * 30)
        else:
            print("No se encontró ningún autor con ese nombre.")

    def buscar_libro_por_titulo(self, titulo):
        encontrados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if encontrados:
            print("\nLibros encontrados:")
            for libro in encontrados:
                libro.mostrar_libro()
                print("-" * 30)
        else:
            print("No se encontró ningún libro con ese título.")


# Datos de ejemplo
autor1 = Autor("Mario Benedetti", "Uruguay", "14/09/1920", "Letras y Filosofía")
autor2 = Autor("Isabel Allende", "Chile", "02/08/1942", "Periodismo y Literatura")
libro1 = Libro("Gracias por el fuego", "Narrativa", "978-9875666372", autor1)
libro2 = Libro("La casa de los espíritus", "Novela", "978-0060883287", autor2)

# Crear biblioteca y cargar datos
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_autor(autor1)
mi_biblioteca.agregar_autor(autor2)
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)


# Interfaz de usuario por consola
def interfaz_busqueda():
    print("\n📚 Bienvenido al sistema de búsqueda de la biblioteca")
    print("Seleccione una opción:")
    print("1. Buscar autor por nombre")
    print("2. Buscar libro por título")
    print("3. Salir")

    while True:
        opcion = input("\nIngrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del autor a buscar: ")
            mi_biblioteca.buscar_autor_por_nombre(nombre)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            mi_biblioteca.buscar_libro_por_titulo(titulo)
        elif opcion == "3":
            print("Gracias por usar la biblioteca. Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar la interfaz
interfaz_busqueda()
