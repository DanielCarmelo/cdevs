# 🎯 Desafío 62
# Crea una clase Musico que tenga un método instrumento y crea dos subclases Guitarrista y Baterista 
# que sobrescriban el método instrumento. Instancia objetos de estas clases y demuestra el polimorfismo.

# Clase base Musico
class Musico:
    def __init__(self, nombre):
        self.nombre = nombre

    def instrumento(self):
        return "No especificado"

# Subclase Guitarrista que sobrescribe el método instrumento
class Guitarrista(Musico):
    def instrumento(self):
        return "Guitarra"

# Subclase Baterista que sobrescribe el método instrumento
class Baterista(Musico):
    def instrumento(self):
        return "Batería"

# modo de uso
if __name__ == "__main__":
    musicos = [
        Guitarrista("Carlos"),
        Baterista("Lucía"),
        Guitarrista("Andrés"),
        Baterista("Sofía")
    ]

    for musico in musicos:
        print(f"{musico.nombre} toca: {musico.instrumento()}")
