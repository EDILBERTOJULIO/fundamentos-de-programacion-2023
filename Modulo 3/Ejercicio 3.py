"""

Doble del par o triple del impar

Dado un número entero N se debe mostrar 2*N si N es par, o 3*N en caso contrario.

Entrada
La entrada contiene una única línea con el valor de N.

Salida
Una única línea con el valor a mostrar según la regla explicada anteriormente.

Ejemplo de entrada
9

Ejemplo de salida
27

"""

N = int(input())

if N % 2 == 0:
        print(N * 2)
else:
        print(N * 3)

