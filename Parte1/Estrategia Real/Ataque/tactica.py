#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from grafo import Grafo

def guardar_ataque(jugador, origen, destino, ejercitos):
    archivo_ataque = open("ataque" + str(jugador) + ".txt", "a")
    archivo_ataque.write(origen + "," + destino + "," + str(ejercitos) + "\n")
    archivo_ataque.close()

def calcular_ejercitos(ciudad, imperio):
    if ciudad in imperio.keys():
        return int(imperio[ciudad]) + 1
    return 1

def calcular_ejercitos_ataque(mapa, imperio, enemigo, ciudades_adyacentes, ciudad_atacante, ciudad_objetivo):
    minimo_ejercitos = calcular_ejercitos(ciudad_objetivo, enemigo)
    delta = imperio[ciudad_atacante] - minimo_ejercitos
    ejercitos_extra = 0
    if delta > 0:
        for ciudad in ciudades_adyacentes:
            if ciudad in enemigo.keys():
                if delta > enemigo[ciudad] and ejercitos_extra > delta - enemigo[ciudad]:
                    ejercitos_extra = delta - enemigo[ciudad]
    return minimo_ejercitos + ejercitos_extra


def conviene_atacar(mapa, ciudades, imperio, enemigo, ciudad_atacante, ciudad_objetivo):
    ejercitos_enemigos = calcular_ejercitos(ciudad_objetivo, enemigo)
    #Si el ataque resulta en derrota o empate no se ataca
    if int(imperio[ciudad_atacante]) <= ejercitos_enemigos:
        return False

    #Si la cantidad de ejercitos que se pierden es menor a la produccion de la
    #ciudad objetivo no se ataca
    if int(imperio[ciudad_atacante]) - ejercitos_enemigos < ciudades[ciudad_objetivo]:
        return False

    return True

def tactica(jugador, mapa, ciudades, imperio1, imperio2):
    if jugador == "1":
        imperio = imperio1
        enemigo = imperio2
    else:
        imperio = imperio2
        enemigo = imperio1

    for ciudad_atacante in imperio.keys():
        ciudades_adyacentes = mapa.get_adyacentes(ciudad_atacante)
        if ciudades_adyacentes:
            objetivos_validos = list(ciudades_adyacentes - imperio.keys())
            for ciudad_objetivo in objetivos_validos:
                if conviene_atacar(mapa, ciudades, imperio, enemigo, ciudad_atacante, ciudad_objetivo):
                    ejercitos_ataque = calcular_ejercitos_ataque(mapa, imperio, enemigo, ciudades_adyacentes, ciudad_atacante, ciudad_objetivo)
                    guardar_ataque(jugador, ciudad_atacante, ciudad_objetivo, ejercitos_ataque)
                    imperio[ciudad_atacante] -= ejercitos_ataque


def main():
    if len(sys.argv) == 8:
        jugador = sys.argv[1]
        archivo_ciudades = open(sys.argv[2], "r")
        archivo_rutas = open(sys.argv[3], "r")
        archivo_imperio1 = open(sys.argv[4], "r")
        archivo_cosecha1 = open(sys.argv[5], "r")
        archivo_imperio2 = open(sys.argv[6], "r")
        archivo_cosecha2 = open(sys.argv[7], "r")

        mapa = Grafo()
        ciudades = {}

        for linea in archivo_ciudades.readlines():
            (ciudad, capacidad) = linea.split(',')
            mapa.agregar_vertice(ciudad)
            ciudades[ciudad] = int(capacidad)

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

        open("ataque" + str(jugador) + ".txt", "w")

        tactica(jugador, mapa, ciudades, imperio1, imperio2)

        archivo_ciudades.close()
        archivo_rutas.close()
        archivo_imperio1.close()
        archivo_cosecha1.close()
        archivo_imperio2.close()
        archivo_cosecha2.close()

    else:
        print('Se necesitan 7 parametros: Numero de jugador, Archivo de ciudades, Archivo de rutas, Archivo de imperio 1, Archivo de cosecha de imperio 1, Archivo de imperio 2, Archivo de cosecha de imperio 2')

if __name__ == "__main__":
    main()
