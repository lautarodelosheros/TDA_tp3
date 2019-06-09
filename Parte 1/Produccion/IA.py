from constantes import *
from grafos import *
from core import *

import random

def determinar_estrategia():
	if(random.uniform(0, 1) <= PROBABILIDAD_ACTITUD_DEFENSIVA):
		return ACTITUD_DEFENSIVA
	return ACTITUD_OFENSIVA


# Calcula cuantos ejercitos pueden ser convertidos en especia. Siempre asegurando que queden ejercitos_extra luego de un ataque
def determinar_especia_obtenible(desventajas_no_criticas, ejercitos_extra):
	
	especia_obtenible_desventajas_no_criticas = 0

	for desventaja in desventajas_no_criticas.items():
		if(desventaja - 1 - ejercitos_extra > 0):
			especia_obtenible_desventajas_no_criticas += desventaja - 1 - ejercitos_extra


	return especia_obtenible_desventajas_no_criticas



def proteger_ciudades_criticas(jugador, cosechas, desventajas_criticas, imperios, ejercitos_extra):
	
	for ciudad, desventaja in desventajas_criticas.items():	
		if(desventaja >= 0):
			cosecha_a_transformar = (numero_cercano_par(desventaja + 1 + ejercitos_extra) / 2)

			if(cosechas[jugador -1] - cosecha_a_transformar < 0):
				cosecha_a_transformar = cosechas[jugador -1]
				ejercitos_nuevos = cosecha_a_transformar * 2
			else:
				ejercitos_nuevos = numero_cercano_par(desventaja + 1 + ejercitos_extra)

			imperios[jugador - 1][ciudad] += ejercitos_nuevos
			cosechas[jugador -1] -= cosecha_a_transformar


def proteger_ciudades_no_criticas(jugador, cosechas, desventajas_criticas, imperios, ejercitos_extra):
	
	for ciudad, desventaja in desventajas_criticas.items():	
		if(desventaja >= 0):
			cosecha_a_transformar = (numero_cercano_par(desventaja + 1 + ejercitos_extra) / 2)

			if(cosechas[jugador -1] - cosecha_a_transformar < 0):
				cosecha_a_transformar = cosechas[jugador -1]
				ejercitos_nuevos = cosecha_a_transformar * 2
			else:
				ejercitos_nuevos = numero_cercano_par(desventaja + 1 + ejercitos_extra)

			imperios[jugador - 1][ciudad] += ejercitos_nuevos
			cosechas[jugador -1] -= cosecha_a_transformar




def transformar_ejercitos_en_especia(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra):

	especia_obtenible = 0

	for ciudad, desventaja in desventajas_no_criticas.items():
		if(desventaja < 0 and (desventaja + 1 + ejercitos_extra) < 0):
			ejercitos_sobrantes = abs(desventaja + ejercitos_extra + 1)
			especia_obtenible += ejercitos_sobrantes
			imperios[jugador - 1][ciudad] -= ejercitos_sobrantes
		
	cosechas[jugador - 1] += especia_obtenible

	return


def actuar(jugador, actitud, imperios, cosechas, ciudades, rutas):

	if(ACTITUD_DEFENSIVA):
		ejercitos_extra = 4
	else:
		ejercitos_extra = 0
	
	desventajas_criticas, desventajas_no_criticas = calcular_desventaja(jugador, ciudades, rutas, imperios)

	proteger_ciudades_criticas(jugador, cosechas, desventajas_criticas, imperios, ejercitos_extra)
	


	#Si llego a la cosecha ganadora no hace nada
	if(cosechas[jugador - 1] >= COSECHA_MINIMA_GANADORA):
		return
	
	if(ACTITUD_DEFENSIVA):
		proteger_ciudades_no_criticas(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra)
		transformar_ejercitos_en_especia(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra)	
	else:
		transformar_ejercitos_en_especia(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra)
	
	
