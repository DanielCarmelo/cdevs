# Clase base Usuario
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        print(f"Usuario nombre: {self.nombre} | apellido: {self.apellido}")

# Subclase Bibliotecario que hereda de Usuario
class Bibliotecario(Usuario):
    def __init__(self, nombre, apellido, seccion, años_experiencia):
        super().__init__(nombre, apellido)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def mostrar_info(self):
        print(f"Bibliotecario: {self.nombre} {self.apellido} | Sección: {self.seccion} | Antigüedad: {self.años_experiencia} años")

# uso
if __name__ == "__main__":
    bibliotecario1 = Bibliotecario("Lucía", "Fernández", "Literatura Infantil", 12)
    bibliotecario1.mostrar_info()
