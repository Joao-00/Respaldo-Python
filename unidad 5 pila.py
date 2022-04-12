#pilas

#tipo de datos abstracto que se apila y desapila por un solo extremo que se denomina cima
#el ultimo elemento que se pone en la pila es el primero en sacar, estructura se le conoce como lifo
#LIFO (last-in, firts out)

#Pila y sus operaciones: apilar, desapilar, vacia y mostrar su contenido

#importar el paquete deque
from collections import deque

#declaracion pila
pila = deque()

i=0
while True:
    i+=1
    # apilar elementos
    pila.append("elemento {}".format(i))
    print("\n Se agrego un elemento a la pila")
    #mostrar pila
    print("\n", pila)
    if input("desea apilar otro elemento [s/n]: ") == "n":
        break

#mostrar pila
print("{}".format(pila))


while len(pila) > 0:
    #desapilar elementos
    elemento = pila.pop()
    print("\n elemento desapilado {}".format(elemento))

    #mostrar pila
    print(pila)
