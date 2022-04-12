#funciones sin retorno de valor

#definicion de la funcion imprime_lista
def imprime_lista(nombre_lista,*cosas):
    print("Lista de " + nombre_lista)
    for cosa in cosas:
        print(cosa)

#llamado a la funcion imprime_lista
imprime_lista ("Herramientas","Martillo","Destornillador","Alicate","Llaves")
