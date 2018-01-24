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
#div_sil_Ejemplo.py

#Autor: Carlos Daniel Hernandez Mena
#Fecha: 29 de Junio del 2014

#Funcion:

#	$ python div_sil_Ejemplo.py

#Sinopsis


#Este programa prueba la funcion div_sil() de la libreria fonetica3
#que divide en silabas una palabra bien escrita en minusculas.

#Bien escrita significa que no se indica su tonica con una mayuscula, de 
#lo contrario esa tonica es tomada como acento grafico, ejemplo:

#	div_sil(cAsa) ==> cá.sa


#Nota: Si el archivo de salida ya existia, este programa lo sobre-escribe
#Nota: Exactamente la primer linea de este programa sirve para manejar la letra Ñ y acentos
#############################################################################################

#Importar modulos necesarios

#Modulo para trabajar con el sistema operativo
import sys

#Añadir el path donde esta la carpeta "fonetica3"
sys.path.append(".")

#Modulo creado por mi donde viene la funcion div_sil()
from fonetica3.div_sil import div_sil

#############################################################################################
#Ejemplos de uso

print div_sil("palabra")

print div_sil("acción")

print div_sil("perro")

print div_sil("excelente")

print div_sil("examen")

print div_sil("peña")

print div_sil("río")

print div_sil("lingüística")

print div_sil("buey")

print div_sil("huía")







