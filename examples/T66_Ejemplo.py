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
#T66_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 06 de Julio del 2015

#Funcion:

#	$ python T66_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion T66() de la libreria fonetica3
#que transcribe una palabra bien escrita en minusculas en Mexbet T66

#Hay que recordar que la funcion T66() es igual a la funcion T50() que 
#se conserva por compatibilidad.

#El numero 66 refleja el numero de simbolos MEXBET utilizados en
#en la transcripcion a nivel fonetico.


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion T66()
from fonetica3.T66 import T66

#############################################################################################
#Ejemplos de uso

print T66("palabra")

print T66("acción")

print T66("pErro")

print T66("excelEnte")

print T66("exámen")

print T66("pEña")

print T66("ñoño")

print T66("itzcOatl")

print T66("iztaccíhuatl")

print T66("SOlos")




