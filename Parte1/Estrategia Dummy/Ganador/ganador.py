#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from grafo import Grafo

def generar_ganador(jugador):
    archivo_ganador = open("ganador.txt", "w")
    archivo_ganador.write("Jugador " + str(jugador) + "\n")
    archivo_ganador.close()

def generar_empate():
    archivo_ganador = open("ganador.txt", "w")
    archivo_ganador.write("Empate\n")
    archivo_ganador.close()

def calcular_ejercitos(imperio):
    ejercitos = 0
    for ciudad in imperio.keys():
        ejercitos += int(imperio[ciudad])
    return ejercitos

def calcular_desempate(mapa, imperio1, cosecha1, imperio2, cosecha2):
    if cosecha1 > cosecha2:
        generar_ganador(1)
        return
    elif cosecha2 > cosecha1:
        generar_ganador(2)
        return

    cantidad_ciudades1 = len(imperio1)
    cantidad_ciudades2 = len(imperio2)

    if cantidad_ciudades1 > cantidad_ciudades2:
        generar_ganador(1)
        return
    elif cantidad_ciudades2 > cantidad_ciudades1:
        generar_ganador(2)
        return

    cantidad_ejercitos1 = calcular_ejercitos(imperio1)
    cantidad_ejercitos2 = calcular_ejercitos(imperio2)

    if cantidad_ejercitos1 > cantidad_ejercitos2:
        generar_ganador(1)
        return
    elif cantidad_ejercitos2 > cantidad_ejercitos1:
        generar_ganador(2)
        return

    generar_empate()

def metropoli_desconectada(imperio, metropoli, mapa):
    for ciudad in mapa.get_adyacentes(metropoli):
        if ciudad in imperio.keys():
            return False
    for ciudad in imperio.keys():
        if metropoli in mapa.get_adyacentes(ciudad):
            return False
    return True

def procesar(ronda, mapa, imperio1, metropoli1, cosecha1, imperio2, metropoli2, cosecha2):
    if cosecha1 >= 100:
        if cosecha1 >= cosecha2:
            generar_ganador(1)
            return
        elif cosecha1 < cosecha2:
            generar_ganador(2)
            return
        else:
            calcular_desempate(mapa, imperio1, cosecha1, imperio2, cosecha2)
            return

    if cosecha2 >= 100:
        generar_ganador(2)
        return

    if metropoli_desconectada(imperio1, metropoli1, mapa):
        generar_ganador(2)
        return

    if metropoli_desconectada(imperio2, metropoli2, mapa):
        generar_ganador(1)
        return

    if ronda >= 50:
        calcular_desempate(mapa, imperio1, cosecha1, imperio2, cosecha2)
        return

def main():
    if len(sys.argv) == 8:
        ronda = int(sys.argv[1])
        archivo_ciudades = open(sys.argv[2], "r")
        archivo_rutas = open(sys.argv[3], "r")
        archivo_imperio1 = open(sys.argv[4], "r")
        archivo_cosecha1 = open(sys.argv[5], "r")
        archivo_imperio2 = open(sys.argv[6], "r")
        archivo_cosecha2 = open(sys.argv[7], "r")

        mapa = Grafo()

        for linea in archivo_ciudades.readlines():
            (ciudad, capacidad) = linea.split(',')
            mapa.agregar_vertice(ciudad)

        for linea in archivo_rutas.readlines():
            (ciudad1, ciudad2, capacidad) = linea.split(',')
            mapa.agregar_arista(ciudad1, ciudad2, int(capacidad))

        imperio1 = {}
        (metropoli1, ejercitos) = archivo_imperio1.readline().split(',')
        for linea in archivo_imperio1.readlines():
            (ciudad, ejercitos) = linea.split(',')
            imperio1[ciudad] = int(ejercitos)

        imperio2 = {}
        (metropoli2, ejercitos) = archivo_imperio2.readline().split(',')
        for linea in archivo_imperio2.readlines():
            (ciudad, ejercitos) = linea.split(',')
            imperio2[ciudad] = int(ejercitos)

        cosecha1 = int(archivo_cosecha1.readline())

        cosecha2 = int(archivo_cosecha2.readline())

        procesar(ronda, mapa, imperio1, metropoli1, cosecha1, imperio2, metropoli2, cosecha2)

        archivo_ciudades.close()
        archivo_rutas.close()
        archivo_imperio1.close()
        archivo_cosecha1.close()
        archivo_imperio2.close()
        archivo_cosecha2.close()

    else:
        print('Se necesitan 7 parametros: Numero de ronda, Archivo de ciudades, Archivo de rutas, Archivo de imperio 1, Archivo de cosecha 1, Archivo de imperio 2, Archivo de cosecha 2')

if __name__ == "__main__":
    main()
