#5. Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.

#Calculo del IMC


print "Introduzca su peso"
peso = input ()
print "Introduzca su altura"
altura = input ()
IMC=peso/altura**2


print "IMC"
print IMC

if IMC<=18.0:
print "Peso demasiado bajo"
elif IMC<=24.9:
print "Su peso es normal felicidades"
elif IMC<=29.9:
print "Tiene sobrepeso, vigile su dieta"
elif IMC>29.9:
print "Obesidad grave, consulte su médico"