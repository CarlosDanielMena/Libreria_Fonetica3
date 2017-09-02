#-*- coding: utf-8 -*-
#############################################################################################
#fonetica3 library provide functions to make phonetic and phonological transcriptions of 
#words in Spanish

#Copyright 2017 Carlos Daniel Hernandez Mena 
#Contact: carlos.mena@ciempiess.org

#This file is part of fonetica3 library

#    fonetica3 library is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    fonetica3 library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with fonetica3 library.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################################
#num_sil_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 13 de Diciembre del 2015

#Funcion:

#	$ python num_sil_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion num_sil() de la libreria fonetica3
#que entrega un entero que representa el numero de silabas que tiene
#la palabra en español que recibe como argumento.


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion num_sil()
from fonetica3.num_sil import num_sil

#############################################################################################
#Ejemplos de uso

print num_sil("palabra")

print num_sil("acción")

print num_sil("perro")

print num_sil("excelente")

print num_sil("examen")

print num_sil("peña")





