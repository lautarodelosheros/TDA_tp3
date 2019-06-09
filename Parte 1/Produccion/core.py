import sys

#Obtiene los parametros necesarios para la ejecucion del programa.
#Lanza una excepcion en caso de que no esten todos.

def obtener_parametros(cantidad_parametros):
	
	if (len(sys.argv) != (cantidad_parametros + 1)):
		raise Exception()

	parametros = []

	for i in range(1, len(sys.argv)):
		parametros.append(sys.argv[i])


	return parametros

def determinar_id_ciudad(nombre_ciudad, equivalencias_ciudad_id):

	return equivalencias_ciudad_id[nombre_ciudad]

def existe_nodo(lista, indice):
	
	try:
		lista[indice]
	except IndexError:
		return False

	return True

def maximo_indice_diccionario(diccionario):
	
	maximo_indice = 0

	for indice, valor in diccionario.items():
		if(maximo_indice < indice):
			maximo_indice = indice

	return maximo_indice

def agregar_ciudad_lista_adyacencia(rutas, id_ciudad_origen, id_ciudad_destino, capacidad):
	
	if(not id_ciudad_origen in rutas):
		rutas[id_ciudad_origen] = {}

	rutas[id_ciudad_origen][id_ciudad_destino] = capacidad

	return



def determinar_imperio(ciudad, imperios):
	if(ciudad in imperios[0]):
		return 1
	return 2


def numero_cercano_par(numero):
	if(numero % 2 == 0):
		return numero
	return numero + 1



def agregar_ataques_potenciales(ataques_potenciales, id_ciudad_destino, ejercitos_enemigos):

	if(not id_ciudad_destino in ataques_potenciales):
		ataques_potenciales[id_ciudad_destino] = 0

	ataques_potenciales[id_ciudad_destino] += ejercitos_enemigos

	return
