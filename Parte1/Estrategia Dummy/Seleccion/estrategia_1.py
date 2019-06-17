from grafo import *
from cola import *

def ejecutar_estrategia_1(grafo_ciudades, diccionario_especias, metropoli, lista_metropolis):
    lista_ciudades_priorizadas_por_mayor_produccion = obtener_ciudades_que_mas_producen(diccionario_especias, lista_metropolis)
    return obtener_ciudades_que_se_conectan_con_metropoli(lista_ciudades_priorizadas_por_mayor_produccion, grafo_ciudades, metropoli)

def obtener_ciudades_que_mas_producen(diccionario_especias, lista_metropolis):
    diccionario_auxiliar = {}

    for ciudad in diccionario_especias:

        if ciudad in lista_metropolis: continue

        cantidad_producida = diccionario_especias[ciudad]

        if cantidad_producida not in diccionario_auxiliar:
            lista_ciudades = []
            lista_ciudades.append(ciudad)
            diccionario_auxiliar[cantidad_producida] = lista_ciudades

        else:
            lista_ciudades = diccionario_auxiliar[cantidad_producida]
            lista_ciudades.append(ciudad)

    lista_cantidades_producidas = list( diccionario_auxiliar.keys() )
    lista_cantidades_producidas.sort()
    lista_cantidades_producidas.reverse()
    lista_ciudades_priorizadas = []

    for cantidad_producida in lista_cantidades_producidas:
        lista_ciudades = diccionario_auxiliar[cantidad_producida]

        for ciudad in lista_ciudades:
            lista_ciudades_priorizadas.append(ciudad)

    return lista_ciudades_priorizadas

def obtener_ciudades_que_se_conectan_con_metropoli(lista_ciudades_priorizadas_por_mayor_produccion, grafo_ciudades, metropoli):
    lista_ciudades_conectadas_con_metropoli = []
    lista_ciudades_no_conectadas_con_metropoli = []

    for ciudad in lista_ciudades_priorizadas_por_mayor_produccion:

        if existe_camino(ciudad, metropoli, grafo_ciudades): lista_ciudades_conectadas_con_metropoli.append(ciudad)

        else: lista_ciudades_no_conectadas_con_metropoli.append(ciudad)

    return lista_ciudades_conectadas_con_metropoli + lista_ciudades_no_conectadas_con_metropoli

def existe_camino(ciudad_1, ciudad_2, grafo_ciudades):
    visitados = set()
    cola = Cola()
    visitados.add(ciudad_1)
    cola.encolar(ciudad_1)

    while not cola.esta_vacia():
        ciudad = cola.desencolar()

        for adyacente in grafo_ciudades.obtener_adyacentes(ciudad):

            if adyacente == ciudad_2: return True

            if adyacente not in visitados:
                visitados.add(adyacente)
                cola.encolar(adyacente)

    return False
