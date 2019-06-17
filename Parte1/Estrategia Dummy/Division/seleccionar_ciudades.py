from generar_archivo_de_salida import generar_archivo_de_salida
from parear_archivos import parear_archivos

def seleccionar_ciudades(archivo_ciudades, archivo_seleccion_1, archivo_seleccion_2):
    lista_imperio_1, lista_imperio_2 = parear_archivos(archivo_ciudades, archivo_seleccion_1, archivo_seleccion_2)
    generar_archivo_de_salida(1, lista_imperio_1)
    generar_archivo_de_salida(2, lista_imperio_2)
