"""""
Me volveré millonario

Supongamos que tengo un dinero ahorrado, digamos $100000 (a esta cantidad
llamémosla C), y supongamos además que un banco me está ofreciendo que, si abro una
cuenta con ellos y no retiro nada de ese dinero en un año, al terminar ese año me ganaré
un interés del 10% (a este porcentaje llamémoslo i), es decir, terminaré con $110000.
Si la tasa de interés es siempre la misma, nunca retiro nada y cada año reinvierto lo
ganado, ¿será que llego a ser millonario algún día?
Soñar no cuesta nada, pero ¿qué te parece si mientras tanto creas un programa para
que, considerando ese esquema de reinversión, dada una cantidad C (expresada en
pesos) y un interés anual i (expresado como fracción, es decir 0.1 = 10%), muestre el
valor final en la cuenta después de transcurridos m años?
Ten en cuenta que la fórmula sería:

final = C * ((1 + i)**𝑚)

Entrada
La entrada contiene tres líneas, la primera con el valor de C, la segunda con el valor de i
y la tercera con el valor de m.

Salida
El valor final pero redondeado al múltiplo de 10 más cercano (esto pues en el sistema
monetario colombiano ya no tenemos monedas de menos de 10 pesos)

Ejemplo de entrada
250000
0.2
10

Ejemplo de salida
1547930.0

"""""
C=int(input())
i=float(input())
m=int(input())

def roundBy(x, base=5):
    return float(base * round(float(x)/base))

print(roundBy((C*((1+i)**m)),10))