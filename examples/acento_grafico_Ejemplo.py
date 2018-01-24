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
#acento_grafico_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 13 de Diciembre del 2015

#Funcion:

#	$ python acento_grafico_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion acento_grafico() de la libreria fonetica3
#que recibe una palabra en español, en minusculas y con su vocal tonica indicada
#con una mayuscula; y al final devuelve la misma palabra pero con su acento grafico 
#si es que lo que requiere, por ejemplo:

#	acento_grafico(canciOn) ==> canción
#	acento_grafico(pErro) ==> perro

#Si la palabra de entrada ya cuenta con una acento grafico, pero en una posicion
#incorrecta, esta funcion ignorara ese acento y decidira ponerlo o no, en base 
#a las reglas de acentuacion del español.

#En las palabras con una sola silaba la decisión de poner o no el acento grafico
#dependera de si la palabra tiene o no su vocal tonica indicada en mayuscula.

#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion acento_grafico()
from fonetica3.acento_grafico import acento_grafico

#############################################################################################
#Ejemplos de uso

print acento_grafico("lingüIstica")

print acento_grafico("canciOn")

print acento_grafico("dEbilmEnte")

print acento_grafico("dEbil")

print acento_grafico("mente")

print acento_grafico("cInica")

print acento_grafico("cInicamente")

print acento_grafico("fomentE")

print acento_grafico("fomEnte")

print acento_grafico("argumEnte")
print acento_grafico("argumentE")

print acento_grafico("sEria")
print acento_grafico("serIa")





