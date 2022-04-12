#conjuntos

#sintaxis:  id_conjunto = {elemento1,elemento2,...,elementoN}               ---- elimina los elementos repetidos
#           id_conjunto = set([elemento1,elemento2,...,elementoN])
#           id_conjunto = frozenset([elemento1,elemento2,...,elementoN])    ---- Para pasar como argumento una lista


#Ejemplos
#conjunto = {1,1,2,3,3,4,5}
#conjunto
#{1,2,3,4,5}

#x = {}
#x
#{}

# ******************NO ENTENDER*****************
#z = {true,"hola",false,"mundo",1,4.0,4,0}
#print(z)
#{false,true,4.0,'mundo','hola'}
#print(hash(true)==hash(1))true
#***********************************************


#ejemplos
#conjunto_set = set ([10,10,22,22,31,31,4,5,])
#conjunto_set
#{4,5,10,22,31}

#conjunto_fro = frozenset([10,10,22,22,31,31,4,5])
#conjunto_fro
#frozenset([4,5,10,22,31])


#s_x = set()
#s_x
#set()


#my_set = {1,1,2,3,7,3,2}
#for s in my_set:
#print(s)
#1
#2
#3
#7

#para saber si el elemento se encuentra en el conjunto
#print(2 in my_set)
#true


#len(my_set)
#4


#creacion del conjunto: my_set
#my-set = {1,3,7,9,11}
#print(my_set)
#{1,3,7,9,11}


#añadiendo un elemento al conjunto
#my_set.add(4)
#print(my_set)
#{1,3,4,7,9,11}


#añadiendo una lista de elementos al conjunto
#my_set.update([1,3,2,6,8])
#print(my_set)
#{1,2,3,4,6,7,8,9,11}


#*******************************************************************
#Estas operaciones solo se aplican a conjuntos mutables

#recibe como parametro el elemento a remover del conjunto
#my_set.remove(3)
#print(my_set)
#{1,2,4,6,7,8,9,11}


#recibe como parametro el elemento a borrar de no existir el elemento no hará nada
#my_set.discard(9)
#print(my_set)
#{1,2,4,6,7,8,11}


#elimina un elemento aleatorio del conjunto y lo muestra
#my_set.pop()
#1
#print(my_set)
#{2,4,6,7,8,11}


#elimina todos los elementos del conjunto
#my_set.clear()
#print(my_set)
#set()
#*******************************************************************


#union
#a = {1,2,3,4}
#b = {4,5,6,7}
#a.union(b)
#{1,2,3,4,5,6,7}
#tambien se puede
#a|b
#{1,2,3,4,5,6,7}


#interseccion
#a.intersection(b)
#{4}
#tambien se puede
#a&b
#{4}


#diferencia
#a.difference(b)
#{1,2,3}
#tambien se puede
#a-b
#{1,2,3}


#Diferencia simetrica
#a.symmetric_difference(b)
#{1,2,3,5,6,7}
#tambien se puede
#a^b
#{1,2,3,5,6,7}



#superconjunto
#a.issuperset(b)
#false
#tambien se puede
#a>=b
#false


#subconjunto
#a.issubset(b)
#false
#tambien se puede
#a<=b
#false


#disjuntos
#a.isdisjoint(b)
#false

