# Define dos variables numéricas que representen el ancho y el largo de un rectángulo.
# Define variables de tipo string que contengan texto explicativo sobre lo que hace el programa.
# Calcula el área del rectángulo (ancho x largo).
# Utiliza tanto variables numéricas como de texto para presentar el resultado de una manera que
# sea fácil de entender para alguien que no está viendo el código.

# Definimos las variables numéricas
ancho = 20  # ancho del rectángulo en unidades
largo = 30  # largo del rectángulo en unidades

# Definimos variables de tipo string
texto_intro = "Este programa calcula el área de un rectángulo."
texto_area = "El área del rectángulo se calcula multiplicando el ancho por el largo."

# Calculamos el área
area = ancho * largo  # asignamos a la variable area el producto del largo y el ancho

# Presentamos el resultado
print(texto_intro)
print(texto_area)
print("├────Largo──────┤   ")
print("┌───────────────┐   ┬")
print("│               │   │") 
print("│     área      │ Ancho")
print("│               │   │")
print("└───────────────┘   ┴")

print("El ancho del rectángulo es: ", (ancho), "unidades.")
print("El largo del rectángulo es: ", (largo), "unidades.")
print("El área del rectángulo es: ", (area),"unidades cuadradas." )
