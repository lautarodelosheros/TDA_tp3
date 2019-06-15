from obtener_parametros import *
from core import *
from normalizar_entradas import *
from grafos import *
from guardar import *


def main():

	try:
		parametros = obtener_parametros(5)
	except:
		print('Faltan parametros, la sintaxis correcta es: Recoleccion <numero_jugador> <archivo_ciudades> <archivo_rutas> <archivo_cosecha> <archivo_imperio>')
		return

	parametros[0] = int(parametros[0])

	numero_jugador, archivo_ciudades, archivo_rutas, archivo_cosecha, archivo_imperio = parametros

	ciudades, equivalencias_ciudad_id, equivalencias_id_ciudad = leer_ciudades(archivo_ciudades)
	cosecha_inicial = leer_cosecha(archivo_cosecha)
	imperio = leer_imperio(archivo_imperio, equivalencias_ciudad_id)
	rutas = leer_rutas(archivo_rutas, equivalencias_ciudad_id, imperio)

	ciudades = filtrar_ciudades_rival(ciudades, imperio, numero_jugador)
	id_fuente = agregar_fuente_especia(ciudades, rutas)

	cosecha_actual = cosecha_inicial + ford_fulkerson(ciudades, rutas, id_fuente, numero_jugador - 1)
	guardar_cosecha(archivo_cosecha, cosecha_actual)

	return 0


if __name__ == '__main__':
  main()


	






