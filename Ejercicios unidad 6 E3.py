#ejercicio 3 juego adivina el numero

from random import randint

x = randint (1,25)

intentos = 0

while intentos < 6:
    numero = int(input("elige un numero entre 1 y 25: "))
    intentos = intentos + 1
    if numero > x:
        print("tu numero esta por encima")
    elif numero < x:
        print("tu numero esta por debajo")
    else:
        break

if numero == x:
    print("felicidades... eres un genio")
    print("lo lograste en {} intentos ".format(intentos))
else:
    print("uy... has perdido, sera en otra oportunidad")
    
        
