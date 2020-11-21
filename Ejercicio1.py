#1.	Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1

import operator

cadenaPalabras = input("Frase:")

listaPalabras = cadenaPalabras.lower().split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

repeticiones = []

for x in range(0, len(listaPalabras)):
    repeticiones.append((listaPalabras[x], frecuenciaPalab[x]))

myList = list(set(repeticiones))

myList = sorted(myList, key=operator.itemgetter(1), reverse=True)


for x in range(0, len(myList)):
    print(tuple (myList[x][0] + ": " + str(myList[x][1])))

    

