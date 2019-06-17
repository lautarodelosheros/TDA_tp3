def parear_archivos(archivo_ciudades, archivo_seleccion_1, archivo_seleccion_2):
    metropoli_1, metropoli_2 = obtener_metropolis(archivo_ciudades)
    lista_imperio_1 = []
    lista_imperio_2 = []
    lista_imperio_1.append(metropoli_1)
    lista_imperio_2.append(metropoli_2)

    with open(archivo_seleccion_1) as archivo_1:
        with open(archivo_seleccion_2) as archivo_2:
            ciudad_1 = archivo_1.readline().rstrip("\n")
            ciudad_2 = archivo_2.readline().rstrip("\n")

            while ciudad_1 and ciudad_2:

                if ciudad_1 != ciudad_2:
                    agregar_ciudades(ciudad_1, ciudad_2, lista_imperio_1, lista_imperio_2)

                ciudad_1 = archivo_1.readline().rstrip("\n")
                ciudad_2 = archivo_2.readline().rstrip("\n")

            if not ciudad_1 and not ciudad_2: return lista_imperio_1, lista_imperio_2

            if ciudad_1:
                agregar_ciudades_restantes(ciudad_1, lista_imperio_1, archivo_1)
                return lista_imperio_1, lista_imperio_2

            agregar_ciudades_restantes(ciudad_2, lista_imperio_2, archivo_2)
            return lista_imperio_1, lista_imperio_2


def obtener_metropolis(archivo_ciudades):
    with open(archivo_ciudades) as archivo_entrada:
        metropoli_1 = archivo_entrada.readline().rstrip("\n").split(",")[0]
        metropoli_2 = archivo_entrada.readline().rstrip("\n").split(",")[0]
        return metropoli_1, metropoli_2

def agregar_ciudades(ciudad_1, ciudad_2, lista_imperio_1, lista_imperio_2):

    if ciudad_1 not in lista_imperio_2: lista_imperio_1.append(ciudad_1)

    if ciudad_2 not in lista_imperio_1: lista_imperio_2.append(ciudad_2)

def agregar_ciudades_restantes(ciudad, lista_imperio, archivo):

    while ciudad:
        lista_imperio.append(ciudad)
        ciudad = archivo.readline().rstrip("\n")
