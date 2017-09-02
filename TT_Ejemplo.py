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
#TT_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 29 de Junio del 2014

#Funcion:

#	$ python TT_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion TT() de la libreria fonetica3
#que transforma una palabra bien escrita en minusculas en 
#un texto que es mas facil de dividir en silabas y que ademas
#tiene inversa.

#TT es el acronimo de "Transformacion del Texto" o "Text Transformation"


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion TT()
from fonetica3.TT import TT

#############################################################################################
#Ejemplos de uso

print TT("palabra")

print TT("acción")

print TT("pErro")

print TT("excelEnte")

print TT("exámen")

print TT("pEña")

print TT("ñoño")

print TT("papalotl")

print TT("itsmo")

print TT("itzcoátl")





