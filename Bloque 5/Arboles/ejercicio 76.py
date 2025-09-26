
@ 


#definir clase nodo
class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

# Crear el nodo raíz
raiz = Nodo(18)

# Añadir nodos hijos
raiz.izq = Nodo(16)
raiz.der = Nodo(20)

# Añadir nodos hijos al nodo izquierdo del raíz
raiz.izq.izq = Nodo(8)
raiz.izq.der = Nodo(10)

# Añadir nodos hijos al nodo derecho del raíz
raiz.der.izq = Nodo(22)
raiz.der.der = Nodo(24)

# Añadir nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
raiz.izq.der.izq = Nodo(6)
raiz.izq.der.der = Nodo(4)

# Añadir nodos hijos al nodo hijo derecho del hijo derecho del raíz
raiz.der.der.izq = Nodo(30)
raiz.der.der.der = Nodo(32)
"""    18
      /   \
    16      20
   / \     /  \
  8  10   22   24
 / \           /  \
6   4         30  32

"""
def print_preorder(raiz):
    if raiz:
        print(raiz.val, end=" ")
        print_preorder(raiz.izq)
        print_preorder(raiz.der)
print("\n Preorder:")        
print_preorder(raiz)  # Salida esperada: 18 16 8 10 6 4 20 22 24 30 32
