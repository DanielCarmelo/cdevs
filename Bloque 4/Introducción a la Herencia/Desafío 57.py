
    # Clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Autor: {self.nombre}")

# Subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

    def mostrar_info(self):
        print(f"Escritor: {self.nombre} | Género literario: {self.genero}")

# Clase base Academico
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

    def mostrar_info_academica(self):
        print(f"Universidad: {self.universidad}")

# Subclase con herencia múltiple: Escritor + Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad)

    def mostrar_info(self):
        print(f"Escritor Académico: {self.nombre} | Género: {self.genero} | Universidad: {self.universidad}")

# Subclase Poeta que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, tipo_de_poesia):
        super().__init__(nombre)
        self.tipo_de_poesia = tipo_de_poesia

    def mostrar_info(self):
        print(f"Poeta: {self.nombre} | Tipo de poesía: {self.tipo_de_poesia}")

# uso ************************************************************************************************
if __name__ == "__main__":
    escritor = Escritor("Mario Benedetti", "Realismo Social")
    escritor.mostrar_info()

    academico = Academico("Universidad de la República")
    academico.mostrar_info_academica()

    escritor_academico = EscritorAcademico("José Enrique Rodó", "Ensayo filosófico", "Universidad de Montevideo")
    escritor_academico.mostrar_info()

    poeta = Poeta("Idea Vilariño", "Poesía íntima y existencial")
    poeta.mostrar_info()
