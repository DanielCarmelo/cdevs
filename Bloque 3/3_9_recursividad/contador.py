
def es_par_o_impar(numero):
    """
    Devuelve una cadena indicando si el número es par o impar.

    Parámetros:
    numero (int): número a evaluar.

    Retorna:
    str: una cadena con el número y su clasificación (par o impar).
    """
    if numero % 2 == 0:
        return f"{numero} - par"
    else:
        return f"{numero} - impar"



def cuenta_regresiva(n):
    """Función recursiva que imprime desde n hasta 0, indicando si cada número es par o impar."""
    if n < 0:
        return  # Caso base para evitar números negativos
    print(es_par_o_impar(n))
    cuenta_regresiva(n - 1)
