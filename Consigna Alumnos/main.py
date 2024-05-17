from os import system
from Package_Strings.strings import *
from data import *
"""
Integrantes:
    - Federico Deniard
    - Lautaro Forzano
    - Bautista Elena
    - Francisco Salceek
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

def menu():
    run = True
    normalizados = False
    while run :

        option = options()
        match(option) :
            case "A" :
                for video in lista_videos:
                    video.dividir_titulo()
                    video.obtener_codigo_url()
                    video.formatear_fecha()
                normalizados = True
            case "B" :
                if normalizados:
                    for i in range(len(lista_videos)):
                        lista_videos[i].mostrar_tema()
                else:
                    print("Debes normalizar los datos")
            case "C" :
                if normalizados:
                    buble_sort(lista_videos)
                else:
                    print("Debes normalizar los datos")
            case "D" :
                if normalizados:
                    print(convertir_visitas(lista_videos))
                else:
                    print("Debes normalizar los datos")
            case "E" :
                if normalizados:
                    indices:list[int] = maxima_visitas(lista_videos)
                    for indice in indices:
                        lista_videos[indice].mostrar_tema()
                else:
                    print("Debes normalizar los datos")
            case "F" :
                if normalizados:
                    indices:list[int] = obtener_codigo(lista_videos)
                    for indice in indices:
                        lista_videos[indice].mostrar_tema()
                else:
                    print("Debes normalizar los datos")
            case "G" :
                if normalizados:
                    colaborador = input("Ingrese un colaborador: ")
                    indices:list[int] = obtener_colaborador(colaborador,lista_videos)
                    if indices == []:
                        print("No encontramos el colaborador :C")
                    else:
                        for indice in indices:
                            lista_videos[indice].mostrar_tema()
                else:
                    print("Debes normalizar los datos")
            case "H" :
                if normalizados:
                    mes = obtener_mes()
                    indices:list[int] = obtener_temas_mes(lista_videos,mes)
                    for indice in indices:
                        lista_videos[indice].mostrar_tema()
                else:
                    print("Debes normalizar los datos")
            case "I" :
                run = False
                
        system("pause")
        system("cls")

menu()