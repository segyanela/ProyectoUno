
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

def mostrar_menu():
    print("Opciones disponibles")
    print("1 - Mostrar Lista de contactos")
    print("2 - Mostrar informacion de un contactos")
    print("3 - Salir")
    

def mostrar_info_contacto():
    print("Ingrese el nombre del contacto a buscar")
    nombrebuscado = input("> ")
    print("Ingrese el apellido del contacto a buscar")
    apellidobuscado = input("> ")

    with open("inputs/Contactos.txt", "r") as archivo:
        for line in archivo:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            
            if nombre == nombrebuscado:
                if apellido == apellidobuscado:
                    print(f"{apellido},{nombre},{telefono}, {email}")
        input()





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
    print("Ingrese telefono:")
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
    with open("inputs/Contactos.txt", "a") as archivo:
    
        archivo.write(contacto.to_linea())

