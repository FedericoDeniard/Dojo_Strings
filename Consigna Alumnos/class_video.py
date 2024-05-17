from datetime import date

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self):
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video

        division_titulo = self.titulo.split(" | Sesión #") 
        colaborador = division_titulo[0]
        sesion = int(division_titulo[1])
        self.sesion = sesion
        self.colaborador = colaborador
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        codigo = self.url_youtube.replace("https://www.youtube.com/watch?v=","")
        self.codigo_url = codigo
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberán dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 

        fecha_formateada = self.fecha_lanzamiento.split("-")
        fecha_formateada = fecha_formateada
        fecha_formateada = date(int(fecha_formateada[0]),int(fecha_formateada[1]),int(fecha_formateada[2]))
        self.fecha_lanzamiento = fecha_formateada