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
#TT_INV_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 29 de Junio del 2014

#Funcion:

#	$ python TT_INV_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion TT_INV() de la libreria fonetica3
#La funcion TT() transforma una palabra bien escrita en minusculas en 
#un texto que es mas facil de dividir en silabas y que ademas
#tiene inversa. TT_INV(), por lol tanto es la inversa de esa funcion TT()

#TT es el acronimo de "Transformacion del Texto" o "Text Transformation"
#e INV es el acronimo de "inversa", es decir que TT_INV es la transformacion
#inversa de texto.


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

#Modulo creado por mi donde viene la funcion TT_INV()
from fonetica3.TT_INV import TT_INV

#############################################################################################
#Ejemplos de uso


print TT("palabra")
print TT_INV("palabra")

print TT("acción")
print TT_INV("ac5iOn")

print TT("perro")
print TT_INV("peRo")

print TT("excelente")
print TT_INV("ex5elente")

print TT("examen")
print TT_INV("examen")

print TT("peña")
print TT_INV("peNa")

print TT("ñoño")
print TT_INV("NoNo")


print TT("itsmo")
print TT_INV("i2mo")

print TT("itzcoátl")
print TT_INV("i3coAT")




