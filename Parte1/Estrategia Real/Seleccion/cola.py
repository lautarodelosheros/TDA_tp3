class Nodo:
    def __init__(self, dato = None, proximo = None):
        self.dato = dato
        self.proximo = proximo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero == None

    def ver_primero(self):
        return None if not self.primero else self.primero.dato

    def encolar(self, dato):
        nuevo = Nodo(dato)

        if self.ultimo:
            self.ultimo.proximo = nuevo
            self.ultimo = nuevo

        else:
            self.primero = nuevo
            self.ultimo = nuevo

    def desencolar(self):

        if not self.primero: return None

        dato = self.primero.dato
        self.primero = self.primero.proximo

        if not self.primero: self.ultimo = None

        return dato
