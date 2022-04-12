#colas

#estructura lineal de datos similar a la pila
#la insercion de elementos se realiza por el final y la eliminacion de elementos es por el inicial
#estructura denominada FIFO(firts-in, firts-out)

#cola y las operaciones encolar, desencolar, cola vacia y mostrar contenido

#importar deque para declarar la cola
from collections import deque

#declaracion de cola
cola = deque()

i=0
while True:
    i+=1
    #encolar elementos
    cola.append("elemento {}".format(i))
    print("\n Se agrego un elemento a la cola")
    print(cola)

    if input("Desea encolar otro elemento [s/n]: ") == "n":
        break

print("**** COLA ****")
print(cola)


#desencolar los elementos

while len(cola) > 0:
    #desencolar elemento
    #popleft permite elminiar el primer elemento de la cola
    elemento = cola.popleft()
    print("elemento desencolado {}".format(elemento))

    #mostrar cola
    print(cola)
    
