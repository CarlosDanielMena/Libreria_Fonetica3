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
#vocal_tonica_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 29 de Junio del 2014

#Funcion:

#	$ python vocal_tonica_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion vocal_tonica() de la libreria fonetica3
#que recibe una palabra bien escrita en minusculas y devuelve la misma
#palabra pero con la vocal tonica indicada en mayuscula.

#Bien escrita significa que no se indica su tonica con una mayuscula, de 
#lo contrario esa tonica es tomada como acento grafico, ejemplo:

#	vocal_tonica(cAsa) ==> cása


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion vocal_tonica()
from fonetica3.vocal_tonica import vocal_tonica

#############################################################################################
#Ejemplos de uso

print vocal_tonica("palabra")

print vocal_tonica("acción")

print vocal_tonica("perro")

print vocal_tonica("excelente")

print vocal_tonica("examen")

print vocal_tonica("peña")

print vocal_tonica("ñoño")

print vocal_tonica("debidamente")

print vocal_tonica("mente")

print vocal_tonica("débilmente")

print vocal_tonica("cancion")
print vocal_tonica("prision")
print vocal_tonica("soltaron")
print vocal_tonica("comentaron")

print vocal_tonica("teorIas")
print vocal_tonica("quiero")

print vocal_tonica("itsmo")






