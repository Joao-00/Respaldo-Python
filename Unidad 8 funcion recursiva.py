#funciones recursivas

#funcion que se llama asi misma


#ejemplo

def cuenta_atras(n):
    if n == 0:
        print("despegando...!")
    else:
        print("n = ",n)
        cuenta_atras(n-1)
#llamando a la funcion

cuenta_atras(3)        
        

