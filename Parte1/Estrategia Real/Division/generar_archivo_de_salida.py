def generar_archivo_de_salida(jugador, lista_ciudades_priorizadas):
    nombre_archivo = "imperio{}.txt".format(jugador)
    with open(nombre_archivo, "w") as archivo_salida:

        for ciudad in lista_ciudades_priorizadas:
            linea = "{},1\n".format(ciudad)
            archivo_salida.write(linea)
