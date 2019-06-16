from constantes import *
from grafos import *
from core import *

import random

#Determina si el jugador en este turno sera ofensivo o defensivo
def determinar_estrategia():
	if(random.uniform(0, 1) <= PROBABILIDAD_ACTITUD_DEFENSIVA):
		return ACTITUD_DEFENSIVA
	return ACTITUD_OFENSIVA

#Determina si el jugador se olvidara o no de algo.
def determinar_olvido():
	if(random.uniform(0, 1) <= PROBABILIDAD_OLVIDO):
		return True
	return False

#Trata de agregar todos los ejercitos que pueda para no quedar vulnerable ante el enemigo.
#Deja un margen de error de ejercitos_extra.
def proteger_ciudades(jugador, cosechas, desventajas_criticas, imperios, ejercitos_extra):
	
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


#Convierte la maxima cantidad de ejercitos en especia siempre dejando ejercitos_extra de margen de error y
#sin quedar en desventaja.
def transformar_ejercitos_en_especia(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra):

	especia_obtenible = 0

	for ciudad, desventaja in desventajas_no_criticas.items():
		if(desventaja < 0 and (desventaja + 1 + ejercitos_extra) < 0 and especia_obtenible < TRANSFORMACION_MAXIMA_EN_ESPECIA):
			ejercitos_sobrantes = abs(desventaja + ejercitos_extra + 1)

			if(especia_obtenible + ejercitos_sobrantes <= TRANSFORMACION_MAXIMA_EN_ESPECIA):
				especia_obtenible += ejercitos_sobrantes
				imperios[jugador - 1][ciudad] -= ejercitos_sobrantes
			else:
				ejercitos_sobrantes = TRANSFORMACION_MAXIMA_EN_ESPECIA - especia_obtenible  
				especia_obtenible = TRANSFORMACION_MAXIMA_EN_ESPECIA
				imperios[jugador - 1][ciudad] -= ejercitos_sobrantes
		
	cosechas[jugador - 1] += especia_obtenible

	return


def actuar(jugador, actitud, imperios, cosechas, ciudades, rutas):

	#Si se defiende deja algunos ejercitos de mas en cada ciudad
	if(actitud == ACTITUD_DEFENSIVA):
		ejercitos_extra = 4
	else:
		ejercitos_extra = 0
	
	desventajas_criticas, desventajas_no_criticas = calcular_desventaja(jugador, ciudades, rutas, imperios)

	#Si no se olvide protege sus ciudades criticas
	se_olvido = determinar_olvido()
	if(not se_olvido):
		proteger_ciudades(jugador, cosechas, desventajas_criticas, imperios, ejercitos_extra)
	


	#Si llego a la cosecha ganadora no hace nada
	if(cosechas[jugador - 1] >= COSECHA_MINIMA_GANADORA):
		return
	
	if(actitud == ACTITUD_DEFENSIVA):
		proteger_ciudades(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra)
	else:
		transformar_ejercitos_en_especia(jugador, cosechas, desventajas_no_criticas, imperios, ejercitos_extra)
	
	
