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



# Función para recorrido inorden e impresión de suma local
def print_inorder(raiz):
    if raiz:
        # Recorrido del subárbol izquierdo
        print_inorder(raiz.izq)

        # Imprime el valor del nodo actual
        print(raiz.val, end=" ")

        # Recorrido del subárbol derecho
        print_inorder(raiz.der)

        # Cálculo seguro de la suma del nodo actual y sus hijos directos
        suma = raiz.val
        if raiz.izq:
            suma += raiz.izq.val
        if raiz.der:
            suma += raiz.der.val

        # Imprime la suma local del nodo actual
        print(f"\nSuma del nodo {raiz.val} con sus hijos: {suma}")

print_inorder(raiz)

