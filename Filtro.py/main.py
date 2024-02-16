import os
import ui.menus as m

import funciones.campers as c


Movistar = {
    "Movistar" : {
        "usuario" : {},
        "rutas" : {},
        "pruebas" : {},
        "salones" : {}, 
        "entrenadores" : {}
    }
}

if __name__ == "__main__":
    isActiveApp = True
    opMainMenu = 0
    header = """
    *************************************
    *       REGISTRO DE PRUEBAS         *
    *************************************
    """
    while(isActiveApp):
        os.system("cls")
        m.mostrar_menu_principal()
        try:
            opMainMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato incorrecto")
        else:
            if (opMainMenu == 1):
                os.system("cls")
                c.regCamper(Movistar)
            
            elif (opMainMenu == 2):
                print(f"GRACIAS POR USAR NUESTRO SERVICIO")
                isActiveApp = False
            os.system("pause")