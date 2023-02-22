"""""
Calor o frío

¿Te ha pasado que vez una temperatura y crees que está haciendo mucho calor, pero
resulta que estaba expresada en grados Fahrenheit (°F) y no en Centígrados (°C)?
Para no seguir teniendo esa confusión, lo mejor será que hagas un programa para hacer
la conversión.

Recuerda que la fórmula es 
°𝐶 = 5/9 (°𝐹 - 32)

Entrada
La entrada contiene una única línea con un valor real (expresado en °F).

Salida
El mensaje (sin comillas ni tildes) 'x grados centigrados', donde x corresponde a la
equivalencia

Ejemplo de entrada
41.0

Ejemplo de salida
5.0 grados centigrados
"""""

TemperaturaF=float(input())
C=(5/9*(TemperaturaF-32))
print(C,"grados centigrados")
