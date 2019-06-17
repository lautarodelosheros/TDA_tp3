from grafo import *
from estrategia_1 import ejecutar_estrategia_1
from estrategia_2 import ejecutar_estrategia_2
from generar_archivo_de_salida import generar_archivo_de_salida

def priorizar_ciudades(jugador, archivo_ciudades, archivo_rutas):
    grafo_ciudades = Grafo(True)
    diccionario_especias = {}
    lista_metropolis = []
    cargar_ciudades(grafo_ciudades, diccionario_especias, lista_metropolis, archivo_ciudades)
    cargar_rutas(grafo_ciudades, archivo_rutas)
    lista_ciudades_priorizadas = obtener_estrategia(jugador)(grafo_ciudades, diccionario_especias, lista_metropolis[ elegir_posicion_metropoli(jugador) ], lista_metropolis)
    generar_archivo_de_salida(jugador, lista_ciudades_priorizadas)

def cargar_ciudades(grafo_ciudades, diccionario_especias, lista_metropolis, archivo_ciudades):
    with open(archivo_ciudades) as archivo_entrada:
        contador_metropoli = 0

        for linea in archivo_entrada:
            ciudad, especia_producida = linea.rstrip("\n").split(",")

            if contador_metropoli <= 1: lista_metropolis.append(ciudad)

            diccionario_especias[ciudad] = int(especia_producida)
            grafo_ciudades.agregar_vertice(ciudad)
            contador_metropoli += 1

def cargar_rutas(grafo_ciudades, archivo_rutas):
    with open(archivo_rutas) as archivo_entrada:

        for linea in archivo_entrada:
            ciudad1, ciudad2, capacidad_transporte = linea.rstrip("\n").split(",")
            grafo_ciudades.agregar_arista(ciudad1, ciudad2, int(capacidad_transporte))

def obtener_estrategia(jugador):
    diccionario_estrategias = {1 : ejecutar_estrategia_1,
                               2 : ejecutar_estrategia_2}

    return diccionario_estrategias[jugador]

def elegir_posicion_metropoli(jugador):
    diccionario_posiciones = {1 : 0,
                              2 : 1}

    return diccionario_posiciones[jugador]
