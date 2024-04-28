import os
from Contactos import funciones 

class Menu():
    def __init__(self, menu):
        self.MENU = menu

    def limpiar_pantalla(self):
        os.system("cls" if os.name == 'nt' else "clear")

    def start(self):
        while True:
            self.mostrar_menu()

    def mostrar_menu(self):
        self.limpiar_pantalla()

        print("\t\t\t\t\t--------------------------------------------------")
        print ("\t\t\t\t\t\tSistema de Gestión de Contactos.")
        print("\t\t\t\t\t--------------------------------------------------")
        print("\t\t\t\t\tOpciones disponibles")
        for index, opcion in enumerate(self.MENU):
            print(f"\t\t\t\t\t{index+1} - {opcion['mensaje']}")
        print("Ingrese una opcion:")
        
        opcion_id = int(input("> "))
        opcion = self.obtener_opcion(opcion_id)
        
        if opcion is None:
            print("Por favor, seleccione una opción válida.")
            input()
            self.mostrar_menu()
        else:
            self.limpiar_pantalla()
            getattr(funciones, opcion["funcion"])()

    def obtener_opcion(self, buscar_id):
        for index, opcion in enumerate(self.MENU):
            if (index + 1) == buscar_id:
                return opcion
        return None