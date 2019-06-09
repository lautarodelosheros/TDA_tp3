from obtener_parametros import *
from core import *
from grafos import *
from guardar import *
from IA import *


def main():

	try:
		parametros = obtener_parametros(7)
	except:
		print('Faltan parametros, la sintaxis correcta es: Recoleccion <numero_jugador> <archivo_ciudades> <archivo_rutas> <archivo_imperio_1> <archivo_cosecha_1> <archivo_imperio_2> <archivo_cosecha_2>')
		return

	parametros[0] = int(parametros[0])

	numero_jugador, archivo_ciudades, archivo_rutas, archivo_imperio_1, archivo_cosecha_1, archivo_imperio_2, archivo_cosecha_2 = parametros

	ciudades, equivalencias_ciudad_id, equivalencias_id_ciudad = leer_ciudades(archivo_ciudades)
	rutas = leer_rutas(archivo_rutas, equivalencias_ciudad_id)



	cosechas = [0, 1]
	imperios = [0, 1]

	cosechas[0] = leer_cosecha(archivo_cosecha_1)
	imperios[0] = leer_imperio(archivo_imperio_1, equivalencias_ciudad_id)

	cosechas[1] = leer_cosecha(archivo_cosecha_2)
	imperios[1] = leer_imperio(archivo_imperio_2, equivalencias_ciudad_id)

	#actitud = determinar_estrategia()
	actitud = ACTITUD_DEFENSIVA

	actuar(numero_jugador, actitud, imperios, cosechas, ciudades, rutas)

	guardar(numero_jugador, imperios, cosechas, RUTA_ARCHIVOS_TEMPORARIOS, equivalencias_id_ciudad)
	
	return 0


if __name__ == '__main__':
  main()


	






