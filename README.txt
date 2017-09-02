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
Changes with respect to the fonetica2 library
#############################################################################################

- Funtion T22() : This function has been deprecated. It has been substituted for the function T29()
- Funtion T50() : This function has been deprecated. It has been substituted for the function T66()

- Function acento_grafico()   : This function has been added
- Function num_sil()          : This function has been added
- Function pos_tonica()       : This function has been added
- Function patron_sil()       : This function has been added

- Function div_sil()      : This function has been updated
- Function vocal_tonica() : This function has been updated
- Function T29()          : This function has been updated
- Function T66()          : This function has been updated

#############################################################################################
Content of the fonetica3_library directory
#############################################################################################

At the fonetica3_library directory you can find 6 different scripts:

- acento_grafico.py : Script for testing the acento_grafico() function.

- div_sil_Ejemplo.py : Script for testing the div_sil() function.

- num_sil_Ejemplo.py : Script for testing the num_sil() function.

- pos_tonica_Ejemplo.py : Script for testing the pos_tonica() function.

- patron_sil_Ejemplo.py : Script for testing the patron_sil() function.

- T29_Ejemplo.py : Script for testing the T29() function.

- T66_Ejemplo.py : Script for testing the T66() function.

- TT_Ejemplo.py : Script for testing the TT() function.

- TT_INV_Ejemplo.py : Script for testing the TT_INV() function.

- vocal_tonica_Ejemplo.py : Script for testing the vocal_tonica() function

And also you can find a directory called fonetica3 that contains all the
functions of the fonetica3 library which are:

- acento_grafico(): Returns the same incoming word but with a graphic accent if it is
                    necessary, for example: acento_grafico(canciOn) ==> canción ; 
                    acento_grafico(pErro) ==> perro. The tonic vowel of the incoming 
                    word must be indicated in uppercase, otherwise this function will
                    return the exact same incoming word with no changes, for example: 
                    acento_grafico(cancion) ==> cancion. If the incoming word has actually 
                    a graphic accent but in an incorrect position, this function will ignore 
                    that accent and it will decide to put or not the graphic accent according 
                    to the standard accentuation rules of the spanish language. For words
                    with just one syllable, the decision of putting or not a graphic accent
                    depends on the word if it has or not its tonic vowel indicated in uppercase 
                   

- vocal_tonica() : Returns the same incoming word but with its tonic vowel in uppercase 
                   (e.g. cAsa, pErro, gAto, etc.). The tonic vowel of the incoming word must 
                   not be indicated in uppercase, otherwise this uppercase letter will be 
                   consider as a graphic accent, for example: div_sil(cAsa) ==> cása
   
- div_sil() : Returns the syllabification of the incoming word. The tonic vowel of the
              incoming word must not be indicated in uppercase, otherwise this uppercase
              letter will be consider as a graphic accent, for example: div_sil(cAsa) ==> cá.sa

- num_sil(): Returns the number of syllables of the incoming word.

- pos_tonica() : Returns an negative integer that represents the syllable where the tonic vowel
                 is from right to left, for example: -1 indicates that the tonic vowel is in the
                 last syllable, -2 represents that the tonic vowel is in the syllable before
                 the last syllable and so on. The incoming word can have its tonic vowel indicated
                 in uppercase or the tonic vowel could be indicated with the graphinc accent.
                 If there is no tonic vowel indicated in the word the function will return a 
                 "None" value. If there are more than one tonica syllable indicated in the
                 incoming word, for example: "clAramEnte", this function will only report
                 the position of the first tonic vowel found from left to rigth that in this case
		 is "A". So, the result in this example would be: pos_tonica("clAramEnte") ==> -4

- patron_sil() : Returns the syllable pattern of the incoming word. A "C" indicates consonant
                 and a "V" indicates vowel. The syllabication is indicated with "." between
                 syllables.
      
- TT() : "TT" is the acronym for "Text Transformation". This function produces reversible 
         text transformations over the incoming word. These transformations are necessary for
         preparing the incoming word for correct phonetic transcription.

- TT_INV() : Produces the reverse transformations made by the TT() function.
   
- T29() : Produces a phonological transcription in Mexbet T29 of the incoming word. Mexbet is an
          ASCII Computational Alphabet for Mexican Spanish.
   
- T66() : Produces a phonetic transcription in Mexbet T66 of the incoming word. Mexbet is an
          ASCII Computational Alphabet for Mexican Spanish.

NOTICE THAT: Each of these functions accept Spanish words in lowercase as arguments. These words 
can have the tonic vowel marked in uppercase or not (e.g. cAldo , aviOn , comida , etc. ), it
depends on the function specification.

#############################################################################################
System Requirements
#############################################################################################

You need to install:

python 2.7

#############################################################################################
INSTRUCTIONS FOR USING THE fonetica3 LIBRARY
#############################################################################################

Every script with the suffix _Ejemplo.py must be placed at the same level of the
fonetica3 directory and you can run them this way:

	$ python <script_name>_Ejemplo.py

This may produce a result in the command line.

For example, to run the script div_sil_Ejemplo.py you go to the Fonetica3_Library directory

	$ cd Fonetica3_Library

An then

	$ python div_sil_Ejemplo.py


This produces:

	pa.la.bra
	ac.ción
	pe.rro
	ex.ce.len.te
	e.xa.men
	pe.ña
	rí.o
	lin.güís.ti.ca
	buey
	huí.a

If you inspect the code of every of these testing programs you will see
lines of code similar to these for adding a function of the fonetica3 directory
into your code:

	#Modulo para trabajar con el sistema operativo
	import sys

	#Añadir el path donde esta la carpeta "fonetica3"
	sys.path.append(".")

	#Modulo creado por mi donde viene la funcion div_sil()
	from fonetica3.div_sil import div_sil

And you also find lines of code like these, for calling a function of the
fonetica3 library from the example program.

	print div_sil("palabra")

Based on these, you can include the functions of the fonetica3 library
easily into your code.


#############################################################################################
      You downloaded the fonetica3 library from the CIEMPIESS-UNAM Project website at

                                 www.ciempiess.org
#############################################################################################

