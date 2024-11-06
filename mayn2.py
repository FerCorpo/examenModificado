import random

def cargar_lista(nombreFichero):
    lista=[]
    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            libreria={}
            cancion, artista,genero = linea.strip().split(" - ")
            libreria["Nombre"]=cancion
            libreria["Artista"]=artista
            libreria["Genero"]=genero
            lista.append(libreria)
    
    return lista
        
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

canciones=cargar_lista("playlist.txt")
agregar_cancion(canciones,"hello cotto","duki","trap")
print(canciones)
#print(buscar_cancion(canciones,"hello cotto"))
eliminar_cancion(canciones,"hello cotto")
guardar_lista(canciones,"playlist.txt")
print(canciones)

#try except
#Comprobar n valores del fichero
#Crear funcion buscar_cancion(lista,nombre) - hecho
#JSON