import math

def guardar_cosecha(archivo_cosecha, cosecha_actual):

	archivo = open(archivo_cosecha, 'w')

	archivo.write(str(int(cosecha_actual)));

	archivo.close()

	return

def guardar_imperio(archivo_imperio, imperio, equivalencias_id_ciudad):
	
	archivo = open(archivo_imperio, 'w')

	for ciudad, ejercitos in imperio.items():
		archivo.write(equivalencias_id_ciudad[ciudad] + ',' + str(ejercitos) + '\n');

	archivo.close()

	return

def guardar(jugador, imperios, cosechas, ruta_archivos, equivalencias_id_ciudad):

	guardar_cosecha(ruta_archivos + 'cosecha'+ str(jugador) + '_temp.txt', cosechas[jugador - 1])
	guardar_imperio(ruta_archivos + 'imperio'+ str(jugador) + '_temp.txt', imperios[jugador - 1], equivalencias_id_ciudad)

	return
