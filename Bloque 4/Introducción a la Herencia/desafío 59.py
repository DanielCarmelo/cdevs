
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



class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.__formato = formato  # e.g.: 'PDF', 'EPUB'
        self.__tamaño_archivo = tamaño_archivo  # En MB

    # metodos get
    def get_formato(self):
        return self.__formato

    def get_tamaño_archivo(self):
        return self.__tamaño_archivo

    # metodos set
    def set_formato(self, nuevo_formato):
        self.__formato = nuevo_formato

    def set_tamaño_archivo(self, nuevo_tamaño):
        self.__tamaño_archivo = nuevo_tamaño

    # Método para mostrar información general
    def mostrar_info(self):
        return (f"Libro digital: '{self.get_titulo()}' por {self.get_autor()} "
                f"(ISBN: {self.get_isbn()}) - Formato: {self.__formato}, "
                f"Tamaño: {self.__tamaño_archivo} MB")
    
# ********************************** cómo la utilizo? :)

# Ejm: crear una Instancia de LibroDigital
libro_digital = LibroDigital("Pedagogía crítica", "Henry Giroux", "9789876543210", "EPUB", 3.2)

# Instancia de EBook con enlace de descarga
ebook = EBook("Aprendizaje significativo", "David Ausubel", "9781234567890", "PDF", 2.5, "https://ejemplo.com/ausubel.pdf")
