import operator
from core import *

def filtrar_ciudades_rival(ciudades, imperio, numero_jugador):

	ciudades_jugador = {}

	ciudades_jugador[numero_jugador - 1] = ciudades[numero_jugador - 1]
	
	for ciudad in range(2, len(ciudades)):
		if(ciudad in imperio):
			ciudades_jugador[ciudad] = ciudades[ciudad]

	return ciudades_jugador


#Agrega una unica fuente que produce y envia la especia a cada ciudad
#Es una transformacion de multiples fuentes a una.

def agregar_fuente_especia(ciudades, rutas):

	id_fuente = maximo_indice_diccionario(ciudades) + 1

	capacidad_fuente = 0

	for ciudad, especia_producida in ciudades.items():
		capacidad_fuente += especia_producida
		agregar_ciudad_lista_adyacencia(rutas, id_fuente, ciudad, especia_producida)


	ciudades[id_fuente] = capacidad_fuente

	return id_fuente

					
