import random
import json

def cargar_lista(nombreFichero):
    lista=[]
    try:
        with open(nombreFichero,"r") as fichero:
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
    with open(archivo,"w") as fichero:
        for librerias in canciones:
            fichero.write(f"{librerias["Nombre"]} - {librerias["Artista"]} - {librerias["Genero"]}\n")
            #fichero.write(f"{cancion} - {artista}\n")
            
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
guardar_lista(canciones,"playlist.txt")
print(canciones)

#try except - hecho
#Comprobar n valores del fichero - hecho
#Crear funcion buscar_cancion(lista,nombre) - hecho
#JSON