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
#T29_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 06 de Julio del 2015

#Funcion:

#	$ python T29_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion T29() de la libreria fonetica3
#que transcribe una palabra bien escrita en minusculas en Mexbet T29

#Hay que recordar que la funcion T29() es igual a la funcion T22() que 
#se conserva por compatibilidad.

#El numero 29 refleja el numero de simbolos MEXBET utilizados en
#en la transcripcion a nivel fonologico.


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion T29()
from fonetica3.T29 import T29

#############################################################################################
#Ejemplos de uso

print T29("palabra")

print T29("acción")

print T29("pErro")

print T29("excelEnte")

print T29("exámen")

print T29("peña")

print T29("ñoño")

print T29("$ilOfono") 

print T29("camagWei")

print T29("escena")

print T29("escisiOn")

print T29("itzcOatl")

print T29("itsmo")


print T29("huitzilihuitl")

print T29("tlAhuac")

print T29("show")







