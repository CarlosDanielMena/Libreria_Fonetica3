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
#pos_tonica_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 13 de Diciembre del 2015

#Funcion:

#	$ python pos_tonica_Ejemplo.py

#Sinopsis

#Este funcion toma como entrada una palabra en español con
#la vocal tonica indicada en mayuscula y devuelve un entero negativo 
#que indica la posicion de la vocal tonica de derecha a izquierda, por ejemplo:
#-1 significa que la tonica esta en la ultima silaba, -2 significa que la tonica
#esta en la penultima silaba y asi sucesivamente.

#La vocal tonica podria tambien estar indicada por medio del acento grafico 
#de la palabra.

#Si no existe ninguna vocal tonica indicada, esta funcion devuelve "None".

#Hay que tener cuidado con los adverbios terminados en "mente" por que
#esta funcion solo da la ubicacion de la tonica que no esta en esa terminacion,
#por ejemplo: "clA.ra.mEn.te" tiene dos tonicas, pero esta funcion dara por
#resultado -4 que es la que esta en pla primera silaba e ignorará la tonica
#que esta en la terminacion "mente"

#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################
#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Modulo para expresiones regulares
import re

#Modulo creado por mi donde viene la funcion div_sil()
from fonetica3.div_sil import div_sil

#Modulo creado por mi donde viene la funcion num_sil()
from fonetica3.num_sil import num_sil

#Modulo creado por mi donde viene la funcion pos_tonica()
from fonetica3.pos_tonica import pos_tonica
#############################################################################################

print pos_tonica("salomé")

print pos_tonica("sí")

print pos_tonica("cAsa")

print pos_tonica("excEso")

print pos_tonica("ambulAncia")

print pos_tonica("esdrújula")

print pos_tonica("clAramente")

print pos_tonica("rapidísimamEnte")

print pos_tonica("clAramEnte")


#############################################################################################
