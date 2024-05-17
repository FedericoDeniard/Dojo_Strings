from os import system
from class_video import *

def validate_option(option: str, options: list) -> bool:
    is_valid = False
    if option in options:
        is_valid = True
    return is_valid

def options() -> str:
    valid_options = "ABCDEFGHI"
    option = input(   "A - Normalizar objetos\n"
                            "B - Mostrar temas\n"
                            "C - Ordenar temas\n"
                            "D - Promedio de vistas\n"
                            "E - Maxima reproduccion\n"
                            "F - Busqueda por codigo\n"
                            "G - Listar por colaborador\n"
                            "H - Listar por mes\n"
                            "I - Salir\n"
                            "- Ingresar una opcion: ")
    option = option.upper()
    while not validate_option(option, valid_options):
        system("cls")
        print("Ingrese un caracter valido")
        option = input(   "A - Normalizar objetos\n"
                            "B - Mostrar temas\n"
                            "C - Ordenar temas\n"
                            "D - Promedio de vistas\n"
                            "E - Máxima reproduccion\n"
                            "F - Búsqueda por codigo\n"
                            "G - Listar por colaborador\n"
                            "H - Listar por mes\n"
                            "I - Salir\n"
                            "- Ingresar una opcion: ")
        option = option.upper()
    return option 

def buble_sort(videos: list[Video]) -> list:
    for i in range(len(videos)):
        for j in range(i,len(videos)):
            if videos[i].sesion > videos[j].sesion:
                videos[i], videos[j] = videos[j], videos[i]

def convertir_visitas(videos: list[Video]) -> str:
    vistas = 0
    for i in range(len(videos)):
        vistas += videos[i].vistas
    promedio = vistas / i
    promedio = promedio / 1000
    promedio = round(promedio)
    promedio = f"{str(promedio)}k"
    return promedio
        
def maxima_visitas(videos:list[Video]) -> list:
    """Compares views from each video

    Args:
        videos (list[Video]): Array with objects

    Returns:
        list: Returns the index of the video or videos with more views
    """
    maxima_visita = 0
    indices = []
    for i in range(len(videos)):
        if videos[i].vistas > maxima_visita:
            maxima_visita = videos[i].vistas
            indices.clear()
            indices.append(i)
        elif videos[i].vistas >= maxima_visita:
            indices.append(i)
    return indices

def obtener_codigo(videos:list[Video], codigo="nick") -> list:
    indices = []
    for i in range(len(videos)):
        if videos[i].codigo_url.count(codigo) > 0:
            indices.append(i)
    return indices

def obtener_colaborador(busqueda: str, videos:list[Video]) -> list:
    indices = []
    busqueda = busqueda.lower()
    for i in range(len(videos)):
        if videos[i].colaborador.lower().count(busqueda) > 0:
            indices.append(i)
    return indices

def obtener_mes() -> int:
    """Convierte el mes de string si a entero, si el usuario escribe el mes en string, si no, comprueba si el mes es correcto y lo devuelve como entero.

    Returns:
        int: numero del mes
    """
    meses_string = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    meses_numerico = [1,2,3,4,5,6,7,8,9,10,11,12]
    while True:
        mes = input("Ingrese el mes: ")
        mes = mes.lower()
        if mes.isalpha() and mes in meses_string:
            indice = meses_string.index(mes)
            mes = meses_numerico[indice]
            break
        elif mes.isdigit() and int(mes) in meses_numerico:
            mes = int(mes)
            break
        else:
            print("El mes no es válido")
    return mes

def obtener_temas_mes(videos:list[Video], mes: int) -> list:
    indices = []
    for i in range(len(videos)):
        if videos[i].fecha_lanzamiento.month == mes:
            indices.append(i)
    return indices



