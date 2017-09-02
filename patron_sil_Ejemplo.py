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
#patron_sil_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 14 de Diciembre del 2015

#Funcion:

#	$ python patron_sil_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion patron_sil() de la libreria fonetica3
#que recibe una palabra en español ya sea bien escrita o con su vocal
#tonica indicada en mayusculas y devuelve el patron silabico de dicha 
#palabra.

#Bien escrita significa que puede llevar acentos, ñ y ü como dicta la
#ortografia española.

#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion patron_sil()
from fonetica3.patron_sil import patron_sil

#############################################################################################
#Ejemplos de uso

print patron_sil("palabra")

print patron_sil("acción")

print patron_sil("perro")

print patron_sil("excelente")

print patron_sil("examen")

print patron_sil("peña")

print patron_sil("casa")





