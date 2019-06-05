import math

def guardar_cosecha(archivo_cosecha, cosecha_actual):

	archivo = open(archivo_cosecha, 'w')

	archivo.write(str(cosecha_actual));

	archivo.close()

	return
