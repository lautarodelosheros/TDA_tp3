import sys
from priorizar_ciudades import priorizar_ciudades

def main():

    if len(sys.argv) == 4:
        jugador = int( sys.argv[1] )
        ciudades = sys.argv[2]
        rutas = sys.argv[3]
        priorizar_ciudades(jugador, ciudades, rutas)

    else:
        print("Se necesitan 4 parámetros")
        exit()

main()
