
from .clases import Contacto


def mostrar_lista_contactos():
    with open("inputs/Contactos.txt", "r") as archivo:
        print("DNI\t\t\t\t APELLIDO Y NOMBRE\t\t\t\t EMAIL")
        print("--------------------------------------------------------")
        for line in archivo:
            x = line.split("-")
            nombre, apellido, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            a = Contacto(apellido, nombre, email)
            a.imprimir_linea()
            
        input()

def mostrar_menu():
    print("Opciones disponibles")
    print("1 - Mostrar Lista de contactos")
    print("2 - Mostrar informacion de un contactos")
    print("3 - Salir")
    

def mostrar_info_contacto():
    print("Ingrese el DNI del contacto a buscar")
    dni = input("> ")


def salir():
    import time
    import sys
    print("Finalizando aplicacion en 2 segundos...")
    time.sleep(2)
    sys.exit()

def agregar_contacto():
    print("Ingrese los datos del nuevo contacto:")
    print("Ingrese el nombre:")
    nombre=input("> ")
    print("Ingrese el apellido:")
    apellido=input("> ")
    print("Ingrese la fecha de ingreso:")
    telefono=input("> ")
    print("Ingrese el email:")
    email=input("> ")

    c = Contacto(
          apellido, nombre, telefono, email
    )

    guardar_contacto(c)
    print("El contacto ha sido guardado!")

    input("Presione enter para continuar...")

def guardar_contacto(contacto):
    print("El contacto a guardar es:", contacto)
    with open("inputs/Contactos.txt", "r") as archivo:
        archivo.write(contacto.to_linea())
    