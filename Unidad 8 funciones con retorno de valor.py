#funciones con retorno de valor

#una funcion que retorna valor tiene la funcion return

def suma_cuadrado (*numeros):
    cuad = 0
    for num in numeros:
        cuad+=num**2
    return cuad

#llamamos a la funcion

sc= suma_cuadrado(1,2,3)
print("La suma de los N cuadrados es: ", sc)


#-------------------------------------------------


#funciones con argumentos multiples

#sintaxis
#los parametros extras se comportan como una lista (son los que llevan * antes del parametro)
#de no tenerlo serían un parametro fijo, y deben ir después de los parametros fijos

# def nombre_funcion (<parametro fijo,*arbitrarios>)
#   instruccion1
#
#   instruccionN
#
#   [return <expresion>]


#ejemplo

def imprime_lista (nombre_lista, *cosas):
    print("Lista de " + nombre_lista)
    for cosa in cosas:
        print(cosa)
#llamando a la funcion imprime_lista
imprime_lista("herramientas","martillo","destornillador","alicate","llaves")


#parametros arbitrarios claves

#sintaxis
#los parametros con doble ** se comportan como un diccionario

#def nombre_funcion(<parametro fijo, *arbitrarios, **claves>):
#   instruccion1
#
#   instruccionN
#
#   [return <expresion>]

#ejemplo

def imprime_libro(nombre_libro, **descripcion):
    print("libro de " + nombre_libro)
    for clave in descripcion:
        print(clave, descripcion[clave])

#llamando a la funcion
imprime_libro("programacion", autor="luis aparicio", paginas=250)

    
