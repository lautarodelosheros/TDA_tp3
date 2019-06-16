from core import *
	
#Permite al jugador saber cuantos ejercitos enemigos podrian atacar cada ciudad propia.
#Las desventajas criticas son las que se dan en ciudades vecinas a su metropolis.
#Las otras son no criticas.
#Desventaja negativa implica que el jugador tiene mas unidades que su enemigo.
def calcular_desventaja(jugador, ciudades, rutas, imperios):

	ciudades_vecina_metropolis = []
	ataques_potenciales = {}

	desventajas_criticas = {}
	desventajas_no_criticas = {}

	oponente = 1 if (jugador == 2) else 2
	metropolis = jugador - 1

	#Determinar cuantos ejercitos pueden atacar a cada ciudad.

	for ciudad_origen, ciudades_destino in rutas.items():
		for ciudad_destino, capacidad in ciudades_destino.items():
			jugador_dueño_origen = determinar_imperio(ciudad_origen, imperios) - 1
			jugador_dueño_destino = determinar_imperio(ciudad_destino, imperios) - 1

			if(jugador_dueño_origen == -1 or jugador_dueño_destino == -1):
				continue

			if(jugador_dueño_origen != jugador_dueño_destino):
				agregar_ataques_potenciales(ataques_potenciales, ciudad_destino, imperios[jugador_dueño_origen][ciudad_origen]) 
					
	#Determinar cuales de esas ciudad son del jugador dado y calcular la desventaja
	#como desventaja = total_tropas_enemigas_vecinas - tropas_propias_en_ciudad.

	#Las desventajas criticas son las dadas en ciudades vecinas a la metropolis.
  
	for ciudad, ataque_potencial in ataques_potenciales.items():
		if(ciudad == metropolis):
			continue

		if(ciudad in imperios[jugador - 1]):
			if(ciudad in rutas and metropolis in rutas[ciudad]):
				desventajas_criticas[ciudad] = ataque_potencial - imperios[jugador - 1][ciudad]
			else:
				desventajas_no_criticas[ciudad] = ataque_potencial - imperios[jugador - 1][ciudad]

	return desventajas_criticas, desventajas_no_criticas
	
