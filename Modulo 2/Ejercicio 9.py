"""""
Volumen del tanque

Un tanque de agua tiene una forma perfectamente cilíndrica. Si inicialmente está
completamente lleno y empieza a vaciarse a una tasa de v metros cúbicos por minuto,
¿Cuál será su volumen después de m minutos? El volumen inicial no lo conocemos, pero
si su radio r y su altura h (ambos expresados en metros).

Ten en cuenta que la fórmula para el volumen de un cilindro es 𝜋𝑟**2h

Para tus cálculos usa el valor de 𝜋 de la librería math y redondea el resultado a tres cifras
decimales

Entrada
La entrada contiene cuatro líneas con los valores de r, h, v, y m en ese orden.

Salida
El valor en metros cúbicos del volumen final del tanque. Este valor no puede ser negativo,
como mínimo será cero (sin cifras decimales).

Ejemplos de entrada Ejemplos de salida
1.5
2.0
3.2
4.0
/////
1.337
--------------
1.5
2.0
3.2
5.0
/////
0

"""""
import math

pi = math.pi
r = float(input())
h = float(input())
v = float(input())
m = float(input())

def razon_cambio(r,h,v,m):
    result = round(((pi * r**2 * h) - v * m), 3)
    return result

result =razon_cambio(r,h,v,m)
if result >= 0:
    print(result)
else:
    print(0)
