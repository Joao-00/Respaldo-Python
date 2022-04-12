#definir y llamar a una funcion

#sintaxis

#def nombre_funcion (<parametro>) --- opcional
#   instruccion 1
#   
#   instruccion N
#
#   [return <expresion>]


#ejemplo

def suma (x,y):
    print(x+y)

def resta (x,y):
    r = (x-y)
    return r

#llamando una funcion

#sintaxis
#nombre_funcion (<arcumentos>)
#           o
#variable = nombre_funcion (<argumentos>)


x=3
y=4

suma(x,y)

a=3
b=4

resultado= resta(a,b)



