import random
import math
from core import *


def leer_ciudades(nombre_archivo):
	
	lista_ciudades = []
	equivalencias_id_ciudad = []
	equivalencias_ciudad_id = {}

	indice = 0

	archivo = open(nombre_archivo, 'r')

	for ciudad in archivo:
		partes = ciudad.rstrip().split(',')
		lista_ciudades.append(int(partes[1]))
		equivalencias_id_ciudad.append(partes[0])
		equivalencias_ciudad_id[partes[0]] = indice 
		indice += 1
	archivo.close()

	return [lista_ciudades, equivalencias_ciudad_id, equivalencias_id_ciudad]


def leer_cosecha(nombre_archivo):
	
	cosecha_actual = 0

	archivo = open(nombre_archivo, 'r')

	cosecha_actual = int(archivo.readline().rstrip())

	archivo.close()

	return cosecha_actual

def leer_imperio(nombre_archivo, equivalencias_ciudad_id):

	imperio = {}

	archivo = open(nombre_archivo, 'r')

	for ciudad in archivo:
		partes = ciudad.rstrip().split(',')

		imperio[equivalencias_ciudad_id[partes[0]]] = int(partes[1])

	archivo.close()

	return imperio

#Las unicas rutas importantes en este paso del juego son las que unen dos ciudades pertenecientes al imperio del jugador

def leer_rutas(nombre_archivo, equivalencias_ciudad_id, imperio):

	rutas = {}

	archivo = open(nombre_archivo, 'r')

	for ciudad in archivo:

		partes = ciudad.rstrip().split(',')
		capacidad_transporte = int(partes[2])

		id_ciudad_origen = determinar_id_ciudad(partes[0], equivalencias_ciudad_id)
		id_ciudad_destino = determinar_id_ciudad(partes[1], equivalencias_ciudad_id)
		
		if(id_ciudad_origen in imperio and id_ciudad_destino in imperio):
			agregar_ciudad_lista_adyacencia(rutas, id_ciudad_origen, id_ciudad_destino, capacidad_transporte)

	archivo.close()

	return rutas



