def generar_archivo_de_salida(jugador, lista_ciudades_priorizadas):
    nombre_archivo = "seleccion{}.txt".format(jugador)
    with open(nombre_archivo, "w") as archivo_salida:

        for ciudad in lista_ciudades_priorizadas:
            linea = "{}\n".format(ciudad)
            archivo_salida.write(linea)    
