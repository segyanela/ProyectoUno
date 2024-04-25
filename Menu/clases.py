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

        print("Opciones disponibles")
        for index, opcion in enumerate(self.MENU):
            print(f"{index+1} - {opcion['mensaje']}")
        print("Ingrese una opcion:")
        
        opcion = self.obtener_opcion(int(input("> ")))
        
        self.limpiar_pantalla()
        getattr(funciones, opcion["funcion"])()
        
    def obtener_opcion(self, buscar_id):
        for index, opcion in enumerate(self.MENU):
            if (index + 1) == buscar_id:
                return opcion