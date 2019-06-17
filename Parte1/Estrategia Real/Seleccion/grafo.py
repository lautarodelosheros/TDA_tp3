import random

"""
Modela el TDA Grafo, el cual puede ser dirigido o no dirigido.
"""
class Grafo:

    """
    Constructor de la clase Grafo.
    Pre: recibe un buleano. Si no recibe nada modela un grafo dirigido, si recibe
    False modela un grafo no dirigido.
    """
    def __init__(self, es_dirigido = True):
        self.vertices = {}
        self.cantidad = 0
        self.es_dirigido = es_dirigido

    """
    Metodo de la clase Grafo que agrega un vertice.
    Pre: recibe un vertice.
    Post: se agrego un nuevo vertice al grafo.
    """
    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}
        self.cantidad +=1

    """
    Metodo de la clase Grafo que agrega un arista.
    Pre: recibe un vertice, un adyacente al vertice y un peso. Si lo ultimo no se
    recibe, el peso es 1.
    Post: si el vertice no esta en el grafo o si el adyacente no esta en el grafo
    o si ya estan conectados se devuelve False, caso contrario devulve True.
    """
    def agregar_arista(self, vertice, adyacente, peso = 1):

        if vertice not in self.vertices: return False

        if self.estan_conectados(vertice, adyacente): return False

        if not self.es_dirigido:

            if adyacente not in self.vertices: return False

            adyacentes_adyacente = self.vertices[adyacente]
            adyacentes_adyacente[vertice] = peso

        adyacentes_vertice = self.vertices[vertice]
        adyacentes_vertice[adyacente] = peso
        return True

    """
    Metodo de la clase Grafo que borra un vertice.
    Pre: recibe el vertice a borrar.
    Post: si el vertice no se encuetra en el grafo, devuelve None, caso contrario
    se devuelve un diccionario que representa los adyacentes a dicho vertice.
    """
    def borrar_vertice(self, vertice):

        if vertice not in self.vertices: return None

        for vertices in self.vertices:
            adyacentes = self.vertices[vertices]

            if vertice in adyacentes:
                adyacentes.pop(vertice)

        self.cantidad -= 1
        return self.vertices.pop(vertice)

    """
    Metodo de la clase Grafo que borra la arista comprendida por vertice y adyacente.
    Pre: recibe un vertice y un adyacente a ese vertice.
    Post: si el vertice o el adyacente no se encuntran en el grafo se devulve -1,
    caso contrario se devuelve el peso de la arista.
    """
    def borrar_arista(self, vertice, adyacente):

        if vertice not in self.vertices: return -1

        adyacentes_vertice = self.vertices[vertice]

        if adyacente not in adyacentes_vertice: return -1

        if not self.es_dirigido:

            if adyacente not in self.vertices: return -1

            adyacentes_adyacente = self.vertices[adyacente]

            if vertice not in adyacentes_adyacente: return -1

            adyacentes_adyacente.pop(vertice)

        peso = adyacentes_vertice.pop(adyacente)
        return peso

    """
    Metodo de la clase Grafo que se fija si un vertice pertenece o no al grafo.
    Pre: recibe un vertice.
    Post: devuelve True si esta, y False si no lo esta.
    """
    def esta_en_grafo(self, vertice):
        return vertice in self.vertices

    """
    Metodo de la clase Grafo que se fija si dos vertices estan conectados.
    Pre: recibe dos vertices.
    Post: devuelve True si lo estan, y False si no lo estan.
    """
    def estan_conectados(self, vertice1, vertice2):

        if vertice1 not in self.vertices: return False

        adyacentes_vertice1 = self.vertices[vertice1]

        if vertice2 not in adyacentes_vertice1: return False

        return True

    """
    Metodo de la clase Grafo que obtiene el peso de una arista.
    Pre: recibe un vertice y un adyacente al vertice.
    Post: si el vertice no pertenece al grafo o si no estan conectados, devuelve -1,
    caso contrario devuelve el peso de la arista.
    """
    def obtener_peso_arista(self, vertice, adyacente):

        if vertice not in self.vertices: return -1

        adyacentes_vertice = self.vertices[vertice]
        return adyacentes_vertice.get(adyacente, -1)

    """
    Metodo de la clase Grafo que obtiene todas las aristas del grafo.
    Post: devuleve una lista de tuplas con todas las aristas del grafo sin que
    aparezcan las conjugadas en el caso de ser un grafo no dirigido.
    """
    def obtener_todas_las_aristas(self):
        lista_aristas = []

        for vertice in self.vertices:
            adyacentes_vertice = self.vertices[vertice]

            for adyacente in adyacentes_vertice:
                peso = adyacentes_vertice[adyacente]

                if not self.es_dirigido:

                    if estan(lista_aristas, vertice, adyacente): continue

                arista = (peso, vertice, adyacente)
                lista_aristas.append(arista)

        return lista_aristas

    """
    Metodo de la clase Grafo que obtiene todos los vertices.
    Post: devuelve una lista que contiene todos los vertices del grafo.
    """
    def obtener_todos_los_vertices(self):
        vertices = self.vertices
        return list(vertices)

    """
    Metodo de la clase Grafo que obtiene un vertice aleatorio.
    Post: devuelve un vertice aleatorio.
    """
    def obtener_vertice_aleatorio(self):
        vertices = self.vertices
        lista_vertices = list(vertices)
        return random.choice(lista_vertices)

    """
    Metodo de la clase Grafo que obtiene todos los adyacentes a un vertice.
    Pre: recibe un vertice.
    Post: devuleve una lista con todos los adyacentes al vertice recibido.
    """
    def obtener_adyacentes(self, vertice):

        if vertice not in self.vertices: return None

        adyacentes_vertice = self.vertices[vertice]
        return list(adyacentes_vertice)

    """
    Metodo de la clase Grafo que obtiene la cantidad de vertices que tiene el grafo.
    Post: devuelve un nomero que representa la cantidad de vertices que tiene el grafo.
    """
    def obtener_cantidad_vertices(self):
        return self.cantidad

    """
    Metodo especial de la clase Grafo que permite iterarlo.
    """
    def __iter__(self):
        return iter(self.vertices)
