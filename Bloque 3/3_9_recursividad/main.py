# Importamos el módulo 'contador', que debe estar en el mismo directorio
import contador

# Solicita número al usuario
numero = int(input("Ingrese un número entero positivo (utilice digitos numericos): "))
numero= int(abs(numero))

print("Iniciando cuenta regresiva...")
    
# Llama a la función de cuenta regresiva del módulo 'contador'
contador.cuenta_regresiva(numero)

# Mensaje especial al llegar a 0
print("¡La cuenta regresiva ha terminado! ")
