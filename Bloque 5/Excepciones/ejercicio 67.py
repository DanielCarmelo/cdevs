# Se inicia un bloque try para intentar ejecutar instrucciones que podrían generar errores
try:
    # Solicita al usuario que ingrese el primer número entero
    # Si el valor ingresado no puede convertirse a entero, se lanzará una excepción ValueError
    num1 = int(input("Ingrese el primer número entero: "))
    
    # Solicita al usuario que ingrese el segundo número entero
    # También puede lanzar ValueError si el dato no es convertible a entero
    num2 = int(input("Ingrese el segundo número entero: "))
    
    # Intenta realizar la división entre los dos números ingresados
    # Si num2 es cero, se lanzará una excepción ZeroDivisionError
    resultado = num1 / num2
    
    # Si no hubo errores, se muestra el resultado de la división
    print(f"El resultado de dividir {num1} entre {num2} es: {resultado}")

# Este bloque captura específicamente el error de división por cero
except ZeroDivisionError:
    # Se informa al usuario que no puede dividir por cero
    print("Error: No se puede dividir por cero. Intente con otro número.")

# Este bloque captura errores de tipo de dato, como ingresar texto en lugar de números
except ValueError:
    # Se informa al usuario que debe ingresar valores numéricos enteros válidos
    print("Error: Debe ingresar valores numéricos enteros válidos.")

# Este bloque captura cualquier otro tipo de error inesperado que no haya sido previsto
except Exception as e:
    # Se muestra un mensaje genérico junto con la descripción del error
    print(f"Ocurrió un error inesperado: {e}")
