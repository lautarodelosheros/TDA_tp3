#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from grafo import Grafo

def main():
    if len(sys.argv) <= 8:
        jugador = sys.argv[1]
        archivo_ciudades = open(sys.argv[2], "r")
        archivo_rutas = open(sys.argv[3], "r")
        archivo_imperio1 = open(sys.argv[4], "r")
        archivo_cosecha1 = open(sys.argv[5], "r")
        archivo_imperio2 = open(sys.argv[6], "r")
        archivo_cosecha2 = open(sys.argv[7], "r")

        archivo_rutas = open("rutas.txt", "r")

        mapa = Grafo()

        for linea in archivo_rutas.readlines():
            (ciudad1, ciudad2, capacidad) = linea.split(',')
            mapa.agregar_arista(ciudad1, ciudad2, int(capacidad))

        archivo_ciudades.close()
        archivo_rutas.close()
        archivo_imperio1.close()
        archivo_cosecha1.close()
        archivo_imperio2.close()
        archivo_cosecha2.close()

    else:
        print('Se necesitan 7 parametros: [numero de jugador], ciudades.txt,rutas.txt,imperio1.txt,cosecha1.txt,imperio2.txt,cosecha2.txt')

if __name__ == "__main__":
    main()
