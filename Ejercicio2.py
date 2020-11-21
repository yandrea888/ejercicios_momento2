#2.	Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.

frase = input("Frase:")
palabras = frase.split()
resultado = {k:palabras.count(k) for k in list(set(palabras))}
print(resultado)