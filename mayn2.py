import random
import json

def cargar_lista(nombreFichero):
    lista=[]
    try:
        with open(nombreFichero,"r", encoding="utf=8") as fichero:
            #cargar contenido del json
            canciones= json.load(fichero)
            #el contenido del json lo guardamos en una variable auxiliar la cual recorremos con un for
            for linea in canciones:
                libreria={}
                libreria["Nombre"]=linea["Nombre"]
                libreria["Artista"]=linea["Artista"]
                libreria["Genero"]=linea["Genero"]
                lista.append(libreria)

        return lista
    except FileNotFoundError:
        print("Ese archivo no existe")
        return []
    except ValueError:
        print("La linea contiene mas de 3 valores por linea")
        return []
        
def agregar_cancion(canciones,cancion,artista,genero):
    if buscar_cancion(canciones,cancion)==False:
        libreria={}
        libreria["Nombre"]=cancion
        libreria["Artista"]=artista
        libreria["Genero"]=genero
        canciones.append(libreria)
    else:
        print("La cancion ya existia")
    
def eliminar_cancion(canciones,cancion):
    if buscar_cancion(canciones,cancion):
        for i in canciones:
            if i["Nombre"]==cancion:
                canciones.remove(i)
                print(f"La cancion {cancion} ha sido eliminada")
    else:
        print("Cancion no encontrada")
        
               
def guardar_lista(canciones,archivo):
    try:
        with open(archivo,"w",encoding="uft-8") as fichero:
            #usando json.dump en este caso nos convierte nuestra lista de diccionarios a formato json en el fichero que le pasamos despues
            #el indent=4 es para hacer que el json nos aparezca mas legible, con saltos de lineas y 4 espacios al iniciar un [] o un {} en la siguiente linea
            json.dump(canciones,fichero,indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ha ocurrido un error {e} al intentar guardar el archivo")
            
def buscar_cancion(canciones,cancion):
    encontrado=False
    for librerias in canciones:
        if librerias["Nombre"]==cancion:
            return True
        else:
            encontrado=False
            
    return encontrado

canciones=cargar_lista("canciones.json")
agregar_cancion(canciones,"hello cotto","duki","trap")
print(canciones)
#print(buscar_cancion(canciones,"hello cotto"))
eliminar_cancion(canciones,"hello cotto")
guardar_lista(canciones,"canciones.json")
print(canciones)

#try except - hecho
#Comprobar n valores del fichero - hecho
#Crear funcion buscar_cancion(lista,nombre) - hecho
#JSON - hecho