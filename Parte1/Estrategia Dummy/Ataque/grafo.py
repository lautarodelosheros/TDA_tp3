class Grafo:

    def __init__(self, diccionario = None):
        if diccionario is None:
            diccionario = {}
        self.diccionario = diccionario

    def get_vertices(self):
        return list(self.diccionario.keys())

    def agregar_vertice(self, vertice):
       if vertice not in self.diccionario:
            self.diccionario[vertice] = []

    def get_aristas(self):
        aristas = []
        for vertice in self.diccionario:
            for arista in self.diccionario[vertice]:
                if arista not in aristas:
                    aristas.append([arista.origen, arista.destino, arista.peso])
        return aristas

    def agregar_arista(self, origen, destino, peso):
        arista = Arista(origen, destino, peso)
        if origen in self.get_vertices():
            self.diccionario[origen].append(arista)
        else:
            self.diccionario[origen] = [arista]

    def get_adyacentes(self, vertice):
        adyacentes = []
        if vertice in self.get_vertices():
            for arista in self.diccionario[vertice]:
                adyacentes.append(arista.destino)
        return adyacentes

class Arista:

    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_peso(self):
        return self.peso
