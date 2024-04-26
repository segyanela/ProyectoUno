
from .clases import Contacto


def mostrar_lista_contactos():
    with open("inputs/Contactos.txt", "r") as archivo:
        print("APELLIDO Y NOMBRE\t\t\t\t TELEFONO \t\t\t\t EMAIL")
        print("--------------------------------------------------------")
        for line in archivo:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            a = Contacto(apellido, nombre, telefono, email)
            a.imprimir_linea()
            
        input()
    

    

def mostrar_info_contacto():
    print("Ingrese el nombre del contacto a buscar")
    nombrebuscado = input("> ")
    print("Ingrese el apellido del contacto a buscar")
    apellidobuscado = input("> ")
    encontro = None

    with open("inputs/Contactos.txt", "r") as archivo:
        for line in archivo:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            

            if nombre == nombrebuscado and apellido == apellidobuscado:
                   encontro = True
                   break
                   
        c = Contacto(apellido, nombre, telefono, email )
        if encontro == True:
            print("APELLIDO Y NOMBRE\t\t\t\t TELEFONO \t\t\t\t EMAIL")
            c.imprimir_linea()
        else:
            print("El contacto no se encuentra agendado.")

        input()
    pass




def eliminar_contacto():
    print("Ingrese el nombre del contacto a eliminar")
    nombrebuscado = input("> ")
    print("Ingrese el apellido del contacto a eliminar")
    apellidobuscado = input("> ")
    encontro = False

    with open("inputs/Contactos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inputs/Contactos.txt", "w") as archivo:
        for line in lines:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            
            if nombre != nombrebuscado or apellido != apellidobuscado:
                archivo.write(line)
            else:
                encontro = True

    if encontro:
        print("El contacto se ha eliminado correctamente.")
    else:
        print("El contacto no se encuentra agendado.")
    input()


def mostrar_opciones():
    opciones = {
        "1" : "Nombre",
        "2" : "Apellido",
        "3" : "Telefono",
        "4" : "Email"
    }

    print("Seleccione un campo a modificar.")
    for numero,opcion in opciones.items():
        print(f"\t{numero} - {opcion}")


def modificar_contacto():
    print("Ingrese el nombre del contacto a modificar")
    nombrebuscado = input("> ")
    print("Ingrese el apellido del contacto a modificar")
    apellidobuscado = input("> ")
    encontro = False

    with open("inputs/Contactos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inputs/Contactos.txt", "w") as archivo:
        for line in lines:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            
            if nombre == nombrebuscado and apellido == apellidobuscado:
                encontro = True
                opcion_valida = False
                while not opcion_valida:
                    print("Seleccione una opción para modificar:")
                    print("1 - Modificar nombre")
                    print("2 - Modificar apellido")
                    print("3 - Modificar telefono")
                    print("4 - Modificar email")
                    opcion = input("> ")
                    
                    if opcion == "1":
                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                        line = f"{apellido}-{nuevo_nombre}-{telefono}-{email}\n"
                        opcion_valida = True
                    elif opcion == "2":
                        nuevo_apellido = input("Ingrese el nuevo apellido: ")
                        line = f"{nuevo_apellido}-{nombre}-{telefono}-{email}\n"
                        opcion_valida = True
                    elif opcion == "3":
                        nuevo_telefono = input("Ingrese el nuevo telefono: ")
                        line = f"{apellido}-{nombre}-{nuevo_telefono}-{email}\n"
                        opcion_valida = True
                    elif opcion == "4":
                        nuevo_email = input("Ingrese el nuevo email: ")
                        line = f"{apellido}-{nombre}-{telefono}-{nuevo_email}\n"
                        opcion_valida = True
                    else:
                        print("Opción inválida. Por favor, ingrese una opción válida.")

                archivo.write(line)
            else:
                archivo.write(line)

    if encontro:
        print("El contacto se ha modificado correctamente.")
    else:
        print("El contacto no se encuentra agendado.")
    input()


   
    if encontro:
        pass            
    else:
        print("El contacto no se encuentra agendado.")
    input()



def salir():
    import time
    import sys
    print("Finalizando aplicacion en 2 segundos...")
    time.sleep(2)
    sys.exit()

import re

def agregar_contacto():
    print("Ingrese los datos del nuevo contacto:")
    print("Ingrese el nombre:")
    nombre = input("> ")
    print("Ingrese el apellido:")
    apellido = input("> ")
    
    telefono_valido = False
    while not telefono_valido:
        print("Ingrese telefono:")
        telefono = input("> ")
        if len(telefono) == 10:
            telefono_valido = True
        else:
            print("El número de teléfono debe tener 10 dígitos. Inténtelo de nuevo.")

    email_valido = False
    while not email_valido:
        print("Ingrese el email:")
        email = input("> ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email_valido = True
        else:
            print("El formato de email es inválido. Por favor, ingrese un email válido. Inténtelo de nuevo.")

    try:
        c = Contacto(apellido, nombre, telefono, email)
        guardar_contacto(c)
        print("El contacto ha sido guardado!")

    except ValueError as ve:
        print("Error:", ve)

def guardar_contacto(contacto):
    print("El contacto a guardar es:", contacto)
    with open("inputs/Contactos.txt", "a") as archivo:
    
        archivo.write(contacto.to_linea())
