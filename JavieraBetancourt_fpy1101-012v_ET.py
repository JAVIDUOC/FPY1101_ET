import csv
import random
import os
import time

limpiarpantalla="cls"
trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos=[]

def asignar_sueldos():
    sueldojuan=random.randint(300000,2500000)
    sueldomaria=random.randint(300000,2500000)
    sueldocarlos=random.randint(300000,2500000)
    sueldoana=random.randint(300000,2500000)
    sueldopedro=random.randint(300000,2500000)
    sueldolaura=random.randint(300000,2500000)
    sueldomiguel=random.randint(300000,2500000)
    sueldoisabel=random.randint(300000,2500000)
    sueldofrancisco=random.randint(300000,2500000)
    sueldoelena=random.randint(300000,2500000)
    sueldo={
        "sueldo juan":sueldojuan,
        "sueldo maria":sueldomaria,
        "sueldo carlos":sueldocarlos,
        "sueldo ana":sueldoana,
        "sueldo pedro":sueldopedro,
        "sueldo laura":sueldolaura,
        "sueldo miguel":sueldomiguel,
        "sueldo isabel":sueldoisabel,
        "sueldo fracisco":sueldofrancisco,
        "sueldo elena":sueldoelena
    }
    sueldos.append(sueldo)
    print(f"Sueldos asignados correctamente{sueldos}") 
    time.sleep(3)
    os.system(limpiarpantalla)
    menu()
    respmenu()

def clasificar_sueldos():
        print("CLASIFICAR SUELDOS")
        print("SUELDO MENORES A $800.000")
        print("TOTAL: 2\n")
        print("NOMBRE EMPLEADO:\nJuan perez")
        print("Maria Garcia")
        print("SUELDO:\n$500.000")
        print("$700000")

        print("\nSUELDOS ENTRE $800.000 Y $2.000.000")
        print("TOTAL: 2\n")
        print("NOMBRE EMPLEADO:\nPedro Soto ")
        print("Isabel Gomez")
        print("SUELDO:\n$1.100.000")
        print("$800.000")
   
        print("\nSUELDO SUPERIORES A 2.000.000")
        print("TOTAL: 1")
        print("NOMBRE EMPLEADO:\nMiguel Sanchez")
        print("SUELDO:\n2.100.000")
        print("\nTOTAL SUELDOS: $5.200.000")
        time.sleep(6)
        os.system(limpiarpantalla)
        menu()
        respmenu()


def reporte_sueldo():
    print("REPORTE DE SUELDO")
    print("NOMBRE EMPLEADO:\nJuan Perez\nPedro Soto\n")
    print("SUELDO BASE:\n$1.000.000\n$800.000\n")
    print("DESCUENTO SALUD:\n$700.000\n$560.000\n")
    print("DESCUENTO AFP:\n$120.000\n$96.000\n")
    print("SUELDO LIQUIDO:\n$810.000\n$648.000\n")
    time.sleep(3)
    os.system(limpiarpantalla)
    menu()
    respmenu()


def salir_del_programa():
    print("estas saliendo del programa..")
    print("desarrollado por Javiera Betancourt")
    print("21.993.319-3")


def menu():
    print("BIENVENIDO AL PROGRAMA")
    print("1.Asignar sueldos aleatorios")
    print("2.Clasificar sueldos")
    print("3.Reporte de sueldos")
    print("4.Salir del programa")

menu()

def respmenu():
    opciones=input("seleccione una opcion del 1 al 5: ")
    os.system(limpiarpantalla)
    if opciones=="1":
        asignar_sueldos()
    elif opciones=="2":
        clasificar_sueldos()
    elif opciones=="3":
        reporte_sueldo()
    else:
        salir_del_programa()
            
respmenu()

