# Desafio Amplía la clase `Autor` para incluir una lista de libros escritos por el autor. Implementa métodos para agregar y eliminar libros de esta lista.


class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad="", libros=None):
        self.nombre = nombre                          # Nombre del autor
        self.nacionalidad = nacionalidad              # Nacionalidad del autor
        self.libros = libros if libros is not None else []  # Lista de libros (evita compartir listas entre instancias)

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        if self.libros:
            for libro in self.libros:
                print(f" - {libro}")
        else:
            print(" (sin libros registrados)")

    # Método para agregar un libro
    def agregar_libros(self):
        nuevo_libro = input("Ingrese el nombre del nuevo libro: ")
        self.libros.append(nuevo_libro)
        print("Nuevo libro agregado:", nuevo_libro)

    # Método para remover un libro
    def remover_libros(self):
        remover_libro = input("Ingrese el nombre del libro que desea remover: ")
        if remover_libro in self.libros:
            self.libros.remove(remover_libro)
            print("Libro eliminado:", remover_libro)
        else:
            print(f"'{remover_libro}' no se encuentra en la lista, por lo que no podrá ser eliminado.")
            
