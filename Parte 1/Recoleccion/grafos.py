from core import *
import queue

def calcular_grafo_residual(rutas):
	
	rutas_grafo_residual = {}

	for ciudad_origen, ciudades_destino in rutas.items():
		for ciudad_destino, capacidad in ciudades_destino.items():
			agregar_ciudad_lista_adyacencia(rutas_grafo_residual, ciudad_origen, ciudad_destino, capacidad)
			agregar_ciudad_lista_adyacencia(rutas_grafo_residual, ciudad_destino, ciudad_origen, 0)

	return rutas_grafo_residual

def actualizar_grafo_residual(rutas, rutas_grafo_residual, cuello_de_botella, trayecto_st):

	ciudad_anterior = trayecto_st[0]

	for i in range(len(trayecto_st) - 1):
		ciudad = trayecto_st[i + 1]

		if(ciudad_anterior in rutas[ciudad]):
			#Es arista forward		
			rutas_grafo_residual[ciudad][ciudad_anterior] -= cuello_de_botella
			rutas_grafo_residual[ciudad_anterior][ciudad] += cuello_de_botella
		else:
			#Es arista backward
			rutas_grafo_residual[ciudad][ciudad_anterior] += cuello_de_botella
			rutas_grafo_residual[ciudad_anterior][ciudad] -= cuello_de_botella		

		ciudad_anterior = ciudad
	


def determinar_cuello_botella(rutas_grafo_residual, trayecto):

	cuello_de_botella = 0
	ciudad_anterior = trayecto[0]

	for i in range(len(trayecto) - 1):
		ciudad = trayecto[i + 1]

		if(rutas_grafo_residual[ciudad][ciudad_anterior] < cuello_de_botella or cuello_de_botella == 0):
			cuello_de_botella = rutas_grafo_residual[ciudad][ciudad_anterior]

		ciudad_anterior = ciudad

	return cuello_de_botella		
		
	
	

def BFS(ciudades, rutas, origen, destino):
	
	visitadas = {}
	capa = queue.Queue()
	ruta_llegada = {}
		

	#Inicializar visitadas
	
	for ciudad, capacidad in ciudades.items():
		visitadas[ciudad] = False

	visitadas[origen] = True
	capa.put(origen)


	#Inicializar las rutas de llegada a la ciudad destino.
	#Es la unica que tiene multiples caminos validos para llegar.

	ruta_llegada[destino] = []

	while(not capa.empty()):
		ciudad = capa.get()

		rutas_salientes = rutas[ciudad]

		for ciudad_destino, capacidad in rutas_salientes.items():
			if(visitadas[ciudad_destino] or capacidad == 0):
				continue

			if(ciudad_destino != destino):
				ruta_llegada[ciudad_destino] = ciudad
				visitadas[ciudad_destino] = True
				capa.put(ciudad_destino)
			else:
				ruta_llegada[ciudad_destino].append(ciudad)

	return ruta_llegada

def determinar_trayecto_st(trayectos_st, origen, destino):

	if(len(trayectos_st[destino]) == 0):
		return False

	trayecto = []

	ciudad = trayectos_st[destino].pop()
	trayecto.append(destino)
	trayecto.append(ciudad)	

	while ciudad != origen:
		ciudad = trayectos_st[ciudad]
		trayecto.append(ciudad)

	return trayecto

	


def ford_fulkerson(ciudades, rutas, origen, destino):
	
	rutas_grafo_residual = calcular_grafo_residual(rutas)

	trayectos_st = BFS(ciudades, rutas_grafo_residual, origen, destino)
	trayecto_st = determinar_trayecto_st(trayectos_st, origen, destino)

	i = 0

	while(trayecto_st):

		cuello_de_botella = determinar_cuello_botella(rutas_grafo_residual, trayecto_st)
		actualizar_grafo_residual(rutas, rutas_grafo_residual, cuello_de_botella, trayecto_st)

		trayecto_st = determinar_trayecto_st(trayectos_st, origen, destino)

		if(not trayecto_st):
			trayectos_st = BFS(ciudades, rutas_grafo_residual, origen, destino)
			trayecto_st = determinar_trayecto_st(trayectos_st, origen, destino)

		i += 1

	flujo_total = 0
	flujos = rutas_grafo_residual[destino]
	for ciudad, flujo in flujos.items():
		flujo_total += flujo
		

	return flujo_total
	

	

	
