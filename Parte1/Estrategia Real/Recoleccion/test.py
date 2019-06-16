from grafos import *

#Estas son algunas funciones de distintas complejidades que sirven para probar que el Ford-Fulkerson ande bien.

def test_ford_fulkerson_1():
	ciudades_ejemplo = {1: 1, 2:1, 3:1, 4:1}
	rutas_ejemplo = {1: {2: 3, 3: 2},
			 2: {3: 5, 4: 2},
			 3: {4: 3},
			 4: {}}

	return ford_fulkerson(ciudades_ejemplo, rutas_ejemplo, 1, 4) == 5

def test_ford_fulkerson_2():
	ciudades_ejemplo = {1: 1, 2:1, 3:1, 4:1, 5:1, 6:1}
	rutas_ejemplo = {1: {2: 10, 3: 10},
			 2: {3: 2, 4: 4, 5: 8},
			 3: {5: 9},
			 4: {6: 10},
			 5: {4: 6, 6: 10},
			 6: {}}

	return ford_fulkerson(ciudades_ejemplo, rutas_ejemplo, 1, 6) == 19


def test_ford_fulkerson_3():
	ciudades_ejemplo = {1: 1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1}
	rutas_ejemplo = {1: {2: 13, 3: 10, 4: 10},
			 2: {5: 24},
			 3: {2: 5, 4:15, 7:7},
			 4: {7: 15},
			 5: {6: 1, 8: 9},
			 6: {7: 6, 8: 13},
			 7: {8: 16},
			 8: {}}

	return ford_fulkerson(ciudades_ejemplo, rutas_ejemplo, 1, 8) == 26

