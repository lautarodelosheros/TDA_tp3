#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from grafo import Grafo

def actualizar_imperio(archivo_imperio, imperio):
    archivo = open(archivo_imperio, "w")
    for ciudad in imperio:
        archivo.write(ciudad + "," + str(imperio[ciudad]) + "\n")
    archivo.close()

def calcular_ejercitos(ciudad, imperio, ataque):
    for (ciudad_atacante, ciudad_objetivo) in ataque.keys():
        if ciudad_atacante == ciudad:
            return imperio[ciudad] - ataque[ciudad_atacante, ciudad_objetivo]
    return imperio[ciudad]

def procesar(mapa, imperio, imperio_enemigo, ataque, ataque_enemigo):
    for (ciudad_atacante, ciudad_objetivo) in ataque.keys():
        ejercitos_defensa = calcular_ejercitos(ciudad_objetivo, imperio_enemigo, ataque_enemigo)
        ejercitos_ataque = ataque[ciudad_atacante, ciudad_objetivo]
        if ejercitos_ataque > ejercitos_defensa:
            if ciudad_atacante in imperio:
                imperio[ciudad_atacante] -= ejercitos_defensa
            imperio[ciudad_objetivo] = ejercitos_ataque - ejercitos_defensa
            del imperio_enemigo[ciudad_objetivo]
        elif ejercitos_ataque == ejercitos_defensa:
            if ciudad_atacante in imperio:
                imperio[ciudad_atacante] -= ejercitos_defensa
            del imperio_enemigo[ciudad_objetivo]
        else:
            if ciudad_atacante in imperio:
                imperio[ciudad_atacante] -= ejercitos_defensa
            imperio_enemigo[ciudad_objetivo] -= ejercitos_defensa

def contienda(mapa, imperio1, imperio2, ataque1, ataque2):
    procesar(mapa, imperio1, imperio2, ataque1, ataque2)
    procesar(mapa, imperio2, imperio1, ataque2, ataque1)

def main():
    if len(sys.argv) == 7:
        archivo_ciudades = open(sys.argv[1], "r")
        archivo_rutas = open(sys.argv[2], "r")
        archivo_imperio1 = open(sys.argv[3], "r")
        archivo_imperio2 = open(sys.argv[4], "r")
        archivo_ataque1 = open(sys.argv[5], "r")
        archivo_ataque2 = open(sys.argv[6], "r")

        mapa = Grafo()

        for linea in archivo_ciudades.readlines():
            (ciudad, capacidad) = linea.split(',')
            mapa.agregar_vertice(ciudad)

        for linea in archivo_rutas.readlines():
            (ciudad1, ciudad2, capacidad) = linea.split(',')
            mapa.agregar_arista(ciudad1, ciudad2, int(capacidad))

        imperio1 = {}
        for linea in archivo_imperio1.readlines():
            (ciudad, ejercitos) = linea.split(',')
            imperio1[ciudad] = int(ejercitos)

        imperio2 = {}
        for linea in archivo_imperio2.readlines():
            (ciudad, ejercitos) = linea.split(',')
            imperio2[ciudad] = int(ejercitos)

        ataque1 = {}
        for linea in archivo_ataque1.readlines():
            (ciudad_atacante, ciudad_objetivo, ejercitos) = linea.split(',')
            ataque1[ciudad_atacante, ciudad_objetivo] = int(ejercitos)

        ataque2 = {}
        for linea in archivo_ataque2.readlines():
            (ciudad_atacante, ciudad_objetivo, ejercitos) = linea.split(',')
            ataque2[ciudad_atacante, ciudad_objetivo] = int(ejercitos)

        contienda(mapa, imperio1, imperio2, ataque1, ataque2)

        actualizar_imperio(sys.argv[3], imperio1)
        actualizar_imperio(sys.argv[4], imperio2)

        archivo_ciudades.close()
        archivo_rutas.close()
        archivo_imperio1.close()
        archivo_imperio2.close()
        archivo_ataque1.close()
        archivo_ataque2.close()

    else:
        print('Se necesitan 6 parametros: Archivo de ciudades, Archivo de rutas, Archivo de imperio 1, Archivo de imperio 2, Archivo de ataque de imperio 1, Arhivo de ataque de imperio 2')

if __name__ == "__main__":
    main()
