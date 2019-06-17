from grafo import *

def ejecutar_estrategia_2(grafo_ciudades, diccionario_especias, metropoli, lista_metropolis):
    return obtener_ciudades_cuyas_rutas_con_la_metropoli_tienen_mucha_capacidad_de_transporte(metropoli, grafo_ciudades)

def obtener_ciudades_cuyas_rutas_con_la_metropoli_tienen_mucha_capacidad_de_transporte(metropoli, grafo_ciudades):
    lista_ciudades_priorizadas_por_conexion_con_metropoli = grafo_ciudades.obtener_adyacentes(metropoli)
    lista_auxiliar = []
    lista_ciudades_priorizadas = []

    for ciudad in lista_ciudades_priorizadas_por_conexion_con_metropoli:
        capacidad_transporte = grafo_ciudades.obtener_peso_arista(ciudad, metropoli)
        lista_auxiliar.append( (capacidad_transporte, ciudad) )

    lista_auxiliar.sort()
    lista_auxiliar.reverse()

    for capacidad_transporte, ciudad in lista_auxiliar:
        lista_ciudades_priorizadas.append(ciudad)

    return lista_ciudades_priorizadas
