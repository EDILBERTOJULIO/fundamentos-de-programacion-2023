"""""
Mal corredor

Tengo un amigo que corre maratones, pero tengo la sospecha que no es muy bueno.
Cuando le pregunto cómo le fue en una carrera nunca me dice en que puesto queda, y
para colmo de males al decirme el tiempo que se demoró lo hace en segundos en vez de
hacerlo en horas:minutos:segundos como todo el mundo. Yo creo que es para que no me
dé cuenta que se demoró mucho.

¿Podrías hacer un programa para llevar a cabo la conversión?

Entrada
La entrada contiene una única línea con el tiempo en segundos (valor entero positivo
menor 100.000).

Salida
El valor correspondiente en formato horas:minutos:segundos. Ten en cuenta que no es
necesario anteceder 0 cuando alguno de los tres elementos es menor que 10, es decir,
una salida como 2:9:7 es correcta y no se debe convertir a 2:09:07.

Ejemplo de entrada
19788

Ejemplo de salida
5:29:48

"""""

userInput = int(input())

m, s = divmod(userInput, 60)
h, m = divmod(m, 60)

print(f'{h}:{m}:{s}')