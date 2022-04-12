#diccionarios
#colecciones de datos con formato especial que permite definir y acceder a los elementos mediante una clave
#sintaxis
#id_diccionario = {clave1:valor1,clave2:valor2,...,claveN:valorN}
#id_diccionario = dict(clave1=valor1,clave2=valor2,...,claveN=valorN)

#ejemplos
#diccionario = {123:"matematica",324:"fisica",215:"quimica",}
#diccionario
#{123:'matematica',324:'fisica',215:'quimica'}


#diccionario = dict(a=1,b=2,c=3)
#diccionario
#{'a':1,'b':2,'c':3}


#dicc = {}
#dicc
#{}


#dicc = dict()
#dicc
#{}


#acceso a valores
#ejemplos

#diccionario[123]
#'matematica'

#diccionario['c']
#3

#d
#{1:'a',2:'b'}
#si no existe el codigo genera error



#insercion de valores

#diccionario
#{123:'matematica',324:'fisica,215:'quimica'}
#diccionario[430] = 'literatura'
#diccionario
#{123:'matematica',324:'fisica,215:'quimica',430:'literatura'}

#dicc = dict()
#dicc['nombre'] = 'pepe'
#dicc
#{'nombre': 'pepe'}

#dicc = dict(a=15,b=0,c=-20)
#dicc
#{'a':15,'b':0,'c':-20}
#dicc['b']=30         --------- en los diccionarios las claves son unicas por lo que si ingresas un valor cuya clave existe lo modificará de lo contrario lo añadirá
#dicc
#{'a':15,'b':30,'c':-20}


#modificacion valores

#dicc
#{'a':15,'b':30,'c':-20}

#dicc['c'] = 0
#dicc
#{'a':15,'b':30,'c':0}

#dicc['a'] = {123,'ABC']
#dicc
#{'a':[123,'ABC'],'b':30,'c':0, 't':-12}


#detectando claves

#dicc
#{'a':[123,'ABC'],'b':30,'c':0, 't':-12}

#'t' in dicc
#true

#'d' in dicc
#false

#123 in dicc
#false



#metodos

#get()
#dicc{1:'a',2:'b'}
#dicc.get(3,0)
#0
#dicc.get(2,0)
#'b'


#dicc.setdefault(3,[3,3])
#[3,3]
#dicc
#{1:'a',2:'b',3:[3,3]}


#update()
#dicc
#{1:'a',15:'T',10:'r'}
#dicc2
#{4:'s',8:'f'}
#dicc.update(dicc2)
#dicc
#{1:'a',15:'T',10:'r',4:'s',8:'f'}


#values()     devuelve la lista con los valores del dicc
#dicc.values()
#dict_values(['a','b',[3,3]])

#keys()       devuelve una lista con las claves del dicc
#dicc.keys()
#dict_keys([(1,'a'),(2,'b'),(3,[3,3])])

#items()      devuelve una lista de tuplas con los elementos clave/valor
#dicc.items()
#dict_items([(1,'a'),(2,'b'),(3,[3,3])])


#copy()
#dicc2 = dicc.copy()
#dicc
#{1:'a',15:'T',10:'r',4:'s',8:'f'}
#dicc2
#{1:'a',15:'T',10:'r',4:'s',8:'f'}


#clear()
#dicc2.clear()
#dicc2
#{}


#pop()
#dicc
#{1:'a',2:'b',3:[3,3]}
#dicc.pop(2)
#'b'
#dicc
#{1:'a',3:[3,3]}



#funciones

#sorted(id_diccionario)
#diccionario
#{123:'matematica',324:'fisica,215:'quimica',430:'literatura'}
#sorted(diccionario)
#[123,215,324,430]

#len(id_diccionario)
#dicc
#{1:'a',2:'b',3:[3,3]}
#len(dicc)
#3

#del(id_diccionario[clave])
#del(dicc[2])
#dicc
#{1:'a',3:[3,3]}


#list()
#list(dicc.keys())
#{1,15,10,4,8}
#list(dicc.values())
#{'a','T','r','s','f'}
#list(dicc.items())
#[(1,'a'),(15,'T'),(10,'r'),(4,'s'),(8,'f')]






