import sys
from seleccionar_ciudades import seleccionar_ciudades

def main():

    if len(sys.argv) == 5:
        ciudades = sys.argv[1]
        rutas = sys.argv[2]
        seleccion_1 = sys.argv[3]
        seleccion_2 = sys.argv[4]
        seleccionar_ciudades(ciudades, seleccion_1, seleccion_2)

    else:
        print("Se necesitan 5 parámetros")
        exit()

main()
