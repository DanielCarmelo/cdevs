1import os
global razon_social_comprador
global rut_comprador
global total
global n_factura


razon_social_emisor = "El charanguito s.r.l." ;
razon_social_comprador="";

direccion="Dr. Armando Zuñigo N° 254, Carmelo, Uruguay"
rut_emisor= 210003270017
rut_comprador=""
descripcion=[]
cantidad=[]
precio=[]
registro=0
opcion=0
n_factura=0

def ingresar_nuevo():
  
    global descripcion,cantidad,precio
 
    print("Porfavor ingrese descripción del artículo")
    descripcion.append(str(input()))
    print("Porfavor ingrese cantidad")
    cantidad.append(int(input()))
    print("Porfavor ingrese precio")
    precio.append(float(input()))

def borrar_ultimo():
  
    global descripcion,cantidad,precio
    print("Seguro desea eliminar el último articulo s/n?")
    if  input().upper()=="S":
        if len(descripcion)>0: descripcion.pop(), print("Descripción de artículo eliminado"/n)
        if len(cantidad)>0: cantidad.pop(), print("Cantidad de artículo eliminado")
        if len(precio)>0: precio.pop(), print("Precio de artículo eliminado, presione cualquier tecla"),input()
        else:
           print("Presione cualquier tecla para volver")
           input()

def ingresar_cliente():
 
    global razon_social_comprador, rut_comprador

    print("Porfavor ingrese Nombre del cliente o Razón Social")
    razon_social_comprador = input()
    print("Porfavor ingrese RUT")
    rut_comprador =str(input())
    if rut_comprador=="": rut_comprador="Consumidor final"

def dibujarfactura(razon_social_comprador,rut_comprador,n_factura):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(razon_social_emisor,"                                    ",rut_emisor)
    print(direccion,"           Factura Electrónica")
    print("                                                         serie A",str(n_factura).ljust(6, "0"))
 
    print("                    ┌────────────────────────────┐")
    print("                    │     ",str(rut_comprador).ljust(16, " "),"     │")
    print("                    └────────────────────────────┘")

    print("Cliente:",razon_social_comprador)
    print("┌───────────────────────────────────┬──────────┬───────────┬──────────────┐")
    print("│Artículo                           │ Cantidad │   Precio  │  Subtotal    │")
    print("├───────────────────────────────────┼──────────┼───────────┼──────────────┤")
    total=0
    for i in range(len(cantidad)):
     
       
      
        print("│",descripcion[i].ljust(33, " "),"│",str(cantidad[i]).rjust(8," "),"│",str(precio[i]).rjust(9," "),"│",str(float(cantidad[i]*precio[i])).rjust(12," "),"│") 
        total=total+(cantidad[i]*precio[i])
        print("├───────────────────────────────────┼──────────┼───────────┼──────────────┤")
    print("├───────────────────────────────────┼──────────┼───────────┼──────────────┤")
    print("│IVA Básico 22%:",str(round((total/1.22)*0.22,2)).rjust(12," "),"      │          │   TOTAL  $│",str(total).rjust(12," "),"│")
    print("└───────────────────────────────────┴──────────┴───────────┴──────────────┘")
    print("IVA al dia - Vencimiento 11/04/2026                    Via Original cliente")
def menuopciones():
    while True:
          try:
               dibujarfactura(razon_social_comprador,rut_comprador,n_factura)
               print("")
               print("___________________________________________________________________________")
               print("")
               print("Menu")
               print("Opción 1: Ingresar datos del cliente")
               print("Opción 2: Ingresar artículo nuevo")
               print("Opción 3: Borrar último artículo ingresado")
               print("Opción 4: Generar archivo de impresión e imprimir factura")
               print("Opción 5: Salir")
               
               opcion = int(input("Por favor, ingrese un número correspondiente a su opción: ")) 
               if opcion == 1: 
                    ingresar_cliente()  
               if opcion == 2:  
                    ingresar_nuevo()  
               if opcion == 3:  
                    borrar_ultimo()
               if opcion == 5:  
                    break

          except ValueError:
                 print("Eso no es un número entero válido. Inténtelo de nuevo.")
                 input("presione cualquier tecla continuar")

menuopciones()
