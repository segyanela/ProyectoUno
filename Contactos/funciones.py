
from .clases_contacto import Contacto
import re

def mostrar_lista_contactos():
    with open("inputs/Contactos.txt", "r") as archivo:
        print("--------------------------------------------------------------------------------------------------------------------")
        print("APELLIDO Y NOMBRE\t\t\t\t\t TELEFONO \t\t\t\t EMAIL")
        print("--------------------------------------------------------------------------------------------------------------------")
        for line in archivo:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            a = Contacto(apellido, nombre, telefono, email)
            a.imprimir_linea()
           
        input("Presione enter para continuar...")

# Búsqueda de un contacto.
def mostrar_info_contacto():
    print("Ingrese el nombre del contacto a buscar (solo letras):")
    nombrebuscado = input("> ")
    while not nombrebuscado.isalpha():
        print("El nombre solo debe contener letras. Inténtelo de nuevo.")
        nombrebuscado = input("> ")
    

    print("Ingrese el apellido del contacto a buscar (solo letras):")
    apellidobuscado = input("> ")
    while not apellidobuscado.isalpha():
        print("El apellido solo debe contener letras. Inténtelo de nuevo.")
        apellidobuscado = input("> ")
    
    encontro = None

    with open("inputs/Contactos.txt", "r") as archivo:
        for line in archivo:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            

            if nombre == nombrebuscado.upper() and apellido == apellidobuscado.upper():
                   encontro = True
                   break
                   
        c = Contacto(apellido, nombre, telefono, email )
        if encontro == True:
            print("APELLIDO Y NOMBRE\t\t\t\t TELEFONO \t\t\t\t EMAIL")
            c.imprimir_linea()
        else:
            print("El contacto no se encuentra agendado.")

        input("Presione enter para continuar...")




def eliminar_contacto():
    print("Ingrese el nombre del contacto a eliminar (solo letras):")
    nombrebuscado = input("> ")
    while not nombrebuscado.isalpha():
        print("El nombre solo debe contener letras. Inténtelo de nuevo.")
        nombrebuscado = input("> ")
    

    print("Ingrese el apellido del contacto a eliminar (solo letras):")
    apellidobuscado = input("> ")
    while not apellidobuscado.isalpha():
        print("El apellido solo debe contener letras. Inténtelo de nuevo.")
        apellidobuscado = input("> ")

    encontro = False

    with open("inputs/Contactos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inputs/Contactos.txt", "w") as archivo:
        for line in lines:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            
            if nombre != nombrebuscado.upper() or apellido != apellidobuscado.upper():
                archivo.write(line)
            else:
                encontro = True

    if encontro:
        print("El contacto se ha eliminado correctamente.")
    else:
        print("El contacto no se encuentra agendado.")
    input("Presione enter para continuar...")


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
    print("Ingrese el nombre del contacto a modificar (solo letras):")
    nombrebuscado = input("> ")
    while not nombrebuscado.isalpha():
        print("El nombre solo debe contener letras. Inténtelo de nuevo.")
        nombrebuscado = input("> ")
    

    print("Ingrese el apellido del contacto a modificar (solo letras):")
    apellidobuscado = input("> ")
    while not apellidobuscado.isalpha():
        print("El apellido solo debe contener letras. Inténtelo de nuevo.")
        apellidobuscado = input("> ")
    
    
    encontro = False

    with open("inputs/Contactos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inputs/Contactos.txt", "w") as archivo:
        for line in lines:
            x = line.split("-")
            apellido, nombre, telefono, email = x[0], x[1], x[2], x[3].replace("\n", "")
            
            if nombre == nombrebuscado.upper() and apellido == apellidobuscado.upper():
                encontro = True
                opcion_valida = False

                while not opcion_valida:
                    mostrar_opciones()
                    opcion = input("> ")
                    
                    if opcion == "1":
                        print("Ingrese el nombre (solo letras):")
                        nombre = input()

                        while not nombre.isalpha():
                            print("El nombre solo debe contener letras. Inténtelo de nuevo.")
                            nombre = input("> ")
                        opcion_valida = True
                    elif opcion == "2":
                         print("Ingrese el apellido (solo letras):")
                         apellido = input("> ")
                         while not apellido.isalpha():
                            print("El apellido solo debe contener letras. Inténtelo de nuevo.")
                            apellido = input("> ")
                         opcion_valida = True
                    elif opcion == "3":
                        telefono_valido = False
                        while not telefono_valido:
                            print("Ingrese telefono:")
                            telefono = input("> ")
                            if len(telefono) == 10:
                                telefono_valido = True
                            else:
                                print("El número de teléfono debe tener 10 dígitos. Inténtelo de nuevo.")
                            opcion_valida = True
                    elif opcion == "4":
                        email_valido = False
                        while not email_valido:
                            print("Ingrese el email:")
                            email = input("> ")
                            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                email_valido = True
                            else:
                                print("El formato de email es inválido. Por favor, ingrese un email válido. Inténtelo de nuevo.")
                        opcion_valida = True
                    else:
                        print("Opción inválida. Por favor, ingrese una opción válida.")
                
                c = Contacto(apellido, nombre, telefono, email)
                line = c.to_linea()
                archivo.write(line)
            else:
                archivo.write(line)

    if encontro:
        print("El contacto se ha modificado correctamente.")
    else:
        print("El contacto no se encuentra agendado.")
    input("Presione enter para continuar...")


def salir():
    import time
    import sys
    print("Finalizando aplicacion en 2 segundos...")
    time.sleep(2)
    sys.exit()


def agregar_contacto():
    print("Ingrese los datos del nuevo contacto:")
    print("Ingrese el nombre (solo letras):")
    nombre = input("> ")

    while not nombre.isalpha():
        print("El nombre solo debe contener letras. Inténtelo de nuevo.")
        nombre = input("> ")

    print("Ingrese el apellido (solo letras):")
    apellido = input("> ")
    while not apellido.isalpha():
        print("El apellido solo debe contener letras. Inténtelo de nuevo.")
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

    input("Presione enter para continuar...")

def guardar_contacto(contacto):
    print("El contacto a guardar es:", contacto)
    with open("inputs/Contactos.txt", "a") as archivo:
    
        archivo.write(contacto.to_linea())