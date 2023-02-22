"""""
La parcela de doña Gloria

Doña Gloria tiene una parcela de forma perfectamente rectangular. La quiere vender,
pero no conoce su área, lo que sí sabe es que uno de los lados del terreno mide X metros
y la diagonal mide Y metros
¿Podrías ayudarle haciendo un programa para calcular el área?

Entrada
La entrada contiene dos líneas, la primera con el valor en metros de uno de los lados y
la segunda con el valor en metros de la diagonal.

Salida
El mensaje (sin comillas ni tildes) 'El area total es de Z metros cuadrados', donde Z es el
valor del área en esa unidad y redondeada a dos cifras decimales.

Ejemplo de entrada
20.5
43.8

Ejemplo de salida
El area total es de 793.48 metros cuadrados

"""""
from math import sqrt

area = None 
catetoConocido = float(input()) 
hipotenusa = float(input())

catetoDesc = sqrt(hipotenusa**2 - catetoConocido**2)
areaRect = round(catetoConocido * catetoDesc, 2)

print(f'El area total es de {areaRect} metros cuadrados')