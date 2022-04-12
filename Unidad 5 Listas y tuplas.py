# Listas y tuplas
#importante, la diferencia es que las tuplas NO pueden ser modificadas
#las tuplas se cierran con parentesis NO corchetes a diferencia de las listas

#Sintaxis
#Id_Lista =  [elemento1, elemento2,... elementoN]

#ejemplo
#flores = ["Rosas", 222, 33.8]
#print(flores)
#['Rosas', 222, 33.8]

#y = []
#print(y)
#[]

#acceder a 1 elemento de la lista

#flores = ["Rosas", 222, 33.8]
#se coloca el numero de la posición del elemento que queremos rescatar
#(desde el 0 siendo este el primer elemento hasta el N-1)
#flores [0]
#'Rosas'
#flores[1]
#222
#flores[2]
#33.8
#importante: si colocas una posición que no existe te marcará ERROR

#se puede llamar al elemento desde numeros negativos, pero acá te entregará el
#resultado en reversa, es decir:     --- (es lo mismo para las tuplas con tupla[indice])
#flores[-1]
#33.8
#flores[-2]
#222
#flores[-3]
#'Rosas'

######### NO sirve para tuplas ###########

#modificar elementos de la lista

#flores = ["Rosas", 222, 33.8]
#si necesitas corregir un valor, con la variable asignación '=' y citando el
#elemento a corregir podrás modificar el contenido
#flores[2] = 75.9
#flores         o utilizas print(flores)
#['Rosas', 222, 75.9]

##########################################


#obtener cantidad de elementos de la lista

#flores = ["Rosas", 222, 33.8]
#len(flores)
#3


#recorrer una lista

#for f in flores:
#   print(f)
#'Rosas'
#222
#33.8



#Concatenar listas

#a = [1,2,3]
#b = [4,5,6]
#c = a + b
#print(c)
#[1,2,3,4,5,6]


######### NO sirve para tuplas ###########

#Repite (*) N veces
#d = [0]*4
#d
#[0,0,0,0]

#f = [1,2,3]*3
#f
#[1,2,3,1,2,3,1,2,3]

#f = f*2
#f
#[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]

##########################################



#Slicing(rebanado)

#ls = ["a","b","c","d","e","f"]
#ls [1:3]  ---> recordar que el final es una posición antes de la indicada
#['b','c']

#ls
#['a','b','c','d','e','f']

#u = ls[1:3]
#u
#['b','c']

#ls [:4]   ---> si la primera posición se omite este tomará desde la posición 0
#['a','b','c','d']

#ls [3:]   ---> si la ultima posición se omite este tomará hasta la última posición
#['d','e','f']


######### NO sirve para tuplas ###########

#append (elemento) = lo añade al final de la lista
#ls.append("Z")
#ls
#['a','b','c','d','e','f','Z']


#extend (lista) = recibe como argumento una lista y la añade al final de la lista actual
#ls1 = [1,2,3]
#ls2 = [4,5,6]
#ls1.extend(ls2)
#print(ls1)
#[1,2,3,4,5,6]

#sort()  = ordena la lista de manera acendente
#ls = [5,7,9,2,0,-1]
#ls.sort()
#ls
#[-1,0,2,5,7,9]

#reverse()  = invierte el orden de una lista
#ls.reverse()
#ls
#[-1,0,2,9,7,5]

#########################################



#count(elemento)  = indica la cantidad de veces que se repite el argumento especificado
#ls = [1,2,3,4,5,6,7,4]
#ls.count(4)
#2


#index (elemento,[indiceInic],[indiceFin]) = entrega la posición en la que se encuentra el elemento
#ls = [-1,0,1,3,4,56,98,4]
#ls.index(4,5)
#7

#tuplas = (1,3,2,5,6,2)
#tupla.index(2)
#2
#tupla.index(2,3,6)
#5


######### NO sirve para tuplas ###########

#insert(indice,elemento) = agrega un elemento a la posición indicada
#ls = [-1,0,1,3,4,56,98,4]
#ls.insert(2,89)
#ls
#[-1,0,89,1,3,4,56,98,4]


#pop(indice) = remueve el elemento indicado y si no se le indica removerá el ultimo ingresado
#ls = [9,59,71,-2,76.5,102]
#e = ls.pop(4)
#ls
#[9,59,71,-2,102]
#e
#76.5


#remove(elemento) = remueve el elemento como argumento, borra su primera aparición
#ls = [9,59,71,-2,102]
#ls.remove(-2)
#ls
#[9,59,71,102]

#del id_lista[indiceInc:indiceFin] = esto sirve para borrar más de 1 elemento en una lista
#ls
#[9,59,71,102]
#del ls[1:4]
#ls
#[9]

###############################################

#listas y funciones
#  Funcion      ls=[5,2,0,8,-2]
#  len()         len(ls) ->  5
#  max()         max(ls) ->  8
#  min()         min(ls) -> -2
#  sum()         sum(ls) -> 13  ---- solo sirve con listas numericas
# list()        list([5,2,0,8,-2]) - convierte en lista una secuencia si no se indica la secuencia convierte en una lista vacia --- NO sirve para tuplas
