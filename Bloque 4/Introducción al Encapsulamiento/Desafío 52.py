class Libro:
    # Constructor: inicializa los atributos privados
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Métodos getter: devuelven el valor de cada atributo
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # Métodos setter: permiten modificar el valor de cada atributo
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn


# ********************************** cómo la utilizo? :)

# Crear una instancia de la clase Libro
libro1 = Libro("1984", "George Orwell", "978-0451524935")

# Acceder a los atributos usando getters
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())

# Modificar los atributos usando setters
libro1.set_titulo("Rebelión en la granja")
libro1.set_autor("George Orwell")
libro1.set_isbn("978-8499890944")

# Verificar los cambios
print("\nDespués de modificar:")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())
