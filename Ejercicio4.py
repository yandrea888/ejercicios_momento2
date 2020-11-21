#4.	Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.

nombres = []
for x in range(0,5):
	nombres.append(input("Escribe un nombre: ").lower())

letra_buscada = input("Qué letra buscas?: ")
cantidad = 0


for nombre in nombres:
	for letra in nombre:
		if letra == letra_buscada:
			cantidad = cantidad + 1
			break
		else:
			cantidad = cantidad

print (cantidad)
print (nombres)