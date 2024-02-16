import os
import main as m
import funciones.campers as c


menuP = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Registro Entrenadores", "Creación Rutas de Entrenamiento", "Gestor de Matriculas", "Modulo de Reportes", "Salir"]
menuReporte = ["Campers Inscritos", "Campers Aprobados", "Entrenadores de Campus", "Campers con bajo rendimiento", "Buscar Ruta de Entrenamiento", "Resumen de Módulos", "Volver"]

import os
import main as main_module

import funciones.campers as campers


menu_principal = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Registro Entrenadores", "Creación Rutas de Entrenamiento", "Gestor de Matrículas", "Módulo de Reportes", "Salir"]
menu_reporte = ["Campers Inscritos", "Campers Aprobados", "Entrenadores de Campus", "Campers con bajo rendimiento", "Buscar Ruta de Entrenamiento", "Resumen de Módulos", "Volver"]

def mostrar_menu_principal():
    campers.cf.checkFile(main_module.Movistar)
    header = """
    *************************************
    * SEGUIMIENTO ACADÉMICO CAMPUSLANDS *
    *************************************
    """
    print(header)
    for i, item in enumerate(menu_principal):
        print(f"{i+1} - {item}")

def mostrar_menu_reporte():
    header = """
    *************************************
    *        MÓDULO DE REPORTES         *
    *************************************
    """

    is_incorrecto = True
    op_menu = 0
    while is_incorrecto:
        os.system("cls")
        print(header)
        for i, item in enumerate(menu_reporte):
            print(f"{i+1} - {item}")
        try:
            op_menu = int(input("Ingrese una opción : "))
        except ValueError:
            print("Tipo de dato incorrecto")
        else:
            if op_menu == 1:
                os.system("cls")
                campers.campersInscritos(main_module.campus)
            elif op_menu == 2:
                os.system("cls")
                campers.campersAprobados(main_module.campus)
            elif op_menu == 4:
                is_incorrecto = False
