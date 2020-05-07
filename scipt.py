import pandas as pd
import sys
import json as js

Alumnos = {"Angel":[], "Pedro" :[], "Miguel" :[], "Mario" :[], "Julio" :[], \
                    "Imanol" :[], "Fernanda" :[], "Lizeth" :[], "Diana" :[], "Diego" :[], \
                    "Fernando" :[], "Oscar" :[], "Daniela" :[], "Karen" :[], "Franco" :[], \
                    "Isabel" :[], "Arick" :[], "Edson" :[], "Manuel" :[], "Arely" :[], "Gaby" :[], \
                    "Lalo" :[], "Saul" :[], "Karl" :[], "Carlos" :[], "Melisa" :[], \
                    "Susana" :[], "Andrea" :[], "Rebeca" :[]}


materias= ["Estadistica","Creatividad","Liderazgo","Estructura de datos",\
                 "Programacion de base de datos"]

op = 0
while op != 4:

    print("1.- Registrar Calificaciones")
    print("2.- Mostrar Calificaciones")
    print("3.- Mostrar alumnos reprobados")
    print("4.- Mostrar Estadistica descriptiva")
    print("5.- Exportar a Archivos CSV o JSON")
    print("6.- Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        for e in Alumnos:
            print("Nombre Alumno:",e)
            for i in materias:
                resultado1 = 0
                resultado1 = int(input("Cual es la calificacion?"))
                Alumnos[e].append(resultado1)
    elif opcion == 2:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index = [materias]
        print("****Calificaciones Generales****")
        print(opcin2.T)
        
    elif opcion == 3:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index = [materias]
        var1 = Alumnos.keys()
        for a in var1:
            variable_control = Alumnos.get(a,())
            print(" ")
            print("Alumno:",a)
            print("Reprobados")
            for e in variable_control:
                if e < 60:
                    print(e)
        
    elif opcion == 4:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index= [materias]
        print("****Pestaña Estadistica****")
        print("Selecciona la opcion que necesite consultar")
        print(" 1.-Estadistica de estudiantes: ")
        print(" 2.-Estadistica por materia: ")
        consulta = int(input("**^^**"))
        if consulta == 1:
            print("*Estadistica por Alumno")
            print(opcin2.describe())
            grabar=open("Estadistica.txt","w")
            grabar.write('% s'%opcin2.describe())
            grabar.close()
            
        elif consulta == 2:
            print("*Estadistica por materia")
            print(opcin2.T.describe())
            grabar=open("Estadistica.txt","w")
            grabar.write('% s'%opcin2.T.describe())
            grabar.close()
        
        else:("Opcion no valida")
            
               
        
        
    elif opcion == 5:
        Archivo_calificaciones = pd.DataFrame(Alumnos)
        Archivo_calificaciones.index= [materias]
        print("****Pestaña Exportar****")
        print("1.- Archivo JSon ")
        print("2.- Archivo CSV ")
        merari=int(input("En que tipo de archivo vas a exportarlo?"))
        if merari == 1:
            Archivo_calificaciones.to_json('Archivo_calificaciones.json', orient="index")#/orient="index"/orient="columna"
            print("Exportado")
        if merari == 2:
            Archivo_calificaciones.to_csv (r'Archivo_calificaciones.csv', index=True, header=True) #No olvidar la extensión
            print("Exportado")
     
     
    elif opcion == 6:
        print("Hasta luego!")
        exit()

    else:("Opcion no valida")
    
    
