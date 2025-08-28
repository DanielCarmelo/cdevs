# Clase base que representa un libro tradicional
class Libro:
    def __init__(self, titulo, autor, isbn):
        # Atributos privados del libro
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Métodos para acceder y modificar los atributos
    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_isbn(self): return self.__isbn
    def set_titulo(self, nuevo_titulo): self.__titulo = nuevo_titulo
    def set_autor(self, nuevo_autor): self.__autor = nuevo_autor
    def set_isbn(self, nuevo_isbn): self.__isbn = nuevo_isbn

# Subclase que representa un libro en formato digital
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        # Llama al constructor de Libro
        super().__init__(titulo, autor, isbn)
        # Nuevos atributos específicos del libro digital
        self.__formato = formato
        self.__tamaño_archivo = tamaño_archivo

    # Métodos para acceder y modificar los nuevos atributos
    def get_formato(self): return self.__formato
    def get_tamaño_archivo(self): return self.__tamaño_archivo
    def set_formato(self, nuevo_formato): self.__formato = nuevo_formato
    def set_tamaño_archivo(self, nuevo_tamaño): self.__tamaño_archivo = nuevo_tamaño

    # Muestra la información completa del libro digital
    def mostrar_info(self):
        return (f"Libro digital: '{self.get_titulo()}' por {self.get_autor()} "
                f"(ISBN: {self.get_isbn()}) - Formato: {self.__formato}, "
                f"Tamaño: {self.__tamaño_archivo} MB")

# Subclase especializada que agrega un enlace de descarga
class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        # Llama al constructor de LibroDigital
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        # Atributo nuevo exclusivo del EBook
        self.__enlace_descarga = enlace_descarga

    # Métodos para acceder y modificar el enlace
    def get_enlace_descarga(self): return self.__enlace_descarga
    def set_enlace_descarga(self, nuevo_enlace): self.__enlace_descarga = nuevo_enlace

    # Sobrescribe el método para mostrar también el enlace de descarga
    def mostrar_info(self):
        return (f"EBook: '{self.get_titulo()}' ({self.get_formato()}, {self.get_tamaño_archivo()} MB)\n"
                f"Autor: {self.get_autor()} | ISBN: {self.get_isbn()}\n"
                f"Descarga: {self.__enlace_descarga}")

# Ejemplo de uso: se crean dos objetos y se muestra su información
if __name__ == "__main__":
    libro_digital = LibroDigital("Pedagogía crítica", "Henry Giroux", "9789876543210", "EPUB", 3.2)
    ebook = EBook("Aprendizaje significativo", "David Ausubel", "9781234567890", "PDF", 2.5, "https://mislibros.com/ausubel.pdf")

    print(libro_digital.mostrar_info())
    print("\n" + ebook.mostrar_info())
