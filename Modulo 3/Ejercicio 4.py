"""""

Menor o mayor de edad

Cuando se es menor de edad, el mayor de los anhelos es ser mayor para hacer lo que
se nos venga en gana. La realidad, sin embargo, es muy diferente.

Escribe un programa para leer una edad E en años. Si dicha edad es inferior a 18 debe
mostrarse el mensaje (sin comillas ni puntuación): 'Tienes E lo siento pero no puedes
hacer lo que quieras', en caso contrario debe mostrarse el mensaje (sin comillas ni
puntuación ni tildes): 'Tienes E sigues sin poder hacer lo que quieras pero ademas tienes
obligaciones'.

Entrada
La entrada contiene una única línea con un valor entero positivo que corresponde a la
edad.

Salida
Una única línea con el mensaje correspondiente a mostrar.
Ejemplos de entrada   //       Ejemplos de salida
16                    //  Tienes 16 lo siento pero no puedes hacer lo que quieras
28                    //  Tienes 28 sigues sin poder hacer lo que quieras pero ademas tienes obligaciones

"""""

E=int(input())

if E<18:
       print(f"Tienes {E} lo siento pero no puedes hacer lo que quieras")
else:
      print(f"Tienes {E} sigues sin poder hacer lo que quieras pero ademas tienes obligaciones")