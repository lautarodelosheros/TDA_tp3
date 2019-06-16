#!/bin/bash

archivo_ciudades="../archivos_prueba/ciudades.txt"
archivo_rutas="../archivos_prueba/rutas.txt"
archivo_seleccion1="sleccion1.txt"
archivo_seleccion2="seleccion2.txt"
archivo_imperio1="imperio1.txt"
archivo_imperio2="imperio2.txt"
archivo_cosecha1="cosecha1.txt"
archivo_cosecha2="cosecha2.txt"
archivo_ataque1="ataque1.txt"
archivo_ataque2="ataque2.txt"
archivo_ganador="ganador.txt"

# genera $archivo_seleccion1
python3 Seleccion/seleccion.py 1 $archivo_ciudades $archivo_rutas

# genera $archivo_seleccion2
python3 Seleccion/seleccion.py 2 $archivo_ciudades $archivo_rutas

# genera $archivo_imperio1 e $archivo_imperio2
python3 Division/division.py $archivo_ciudades $archivo_rutas $archivo_seleccion1 $archivo_seleccion2
ronda=1
while [ $ronda -le 50 ]; do
  # genera $archivo_cosecha1
	python3 Recoleccion/recoleccion.py 1 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha1

	# genera $archivo_cosecha2
	python3 Recoleccion/recoleccion.py 2 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha1

	# genera cosecha1_temp.txt e imperio1_temp.txt
	python3 Produccion/produccion.py 1 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha2

	# genera cosecha2_temp.txt e imperio2_temp.txt
	python3 Produccion/produccion.py 2 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha2

	# Renombrar imperio1_temp.txt a $archivo_imperio1
	# Renombrar imperio2_temp.txt a $archivo_imperio2
	# Renombrar cosecha1_temp.txt a $archivo_cosecha1
	# Renombrar cosecha2_temp.txt a $archivo_cosecha2

	# genera el archivo $archivo_ataque1
	python3 Ataque/tactica.py 1 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha2

	# genera el archivo $archivo_ataque2
	python3 Ataque/tactica.py 2 $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha2

	# Actualiza $archivo_imperio1 e $archivo_imperio2
	python3 Contienda/contienda.py $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_imperio2 $archivo_ataque1 $archivo_ataque2

	# determina si hay ganador
	python3 Ganador/ganador.py $ronda $archivo_ciudades $archivo_rutas $archivo_imperio1 $archivo_cosecha1 $archivo_imperio2 $archivo_cosecha2

  if [ -f $archivo_ganador ]; then
    break
  fi

  ronda=$((ronda + 1))

done
