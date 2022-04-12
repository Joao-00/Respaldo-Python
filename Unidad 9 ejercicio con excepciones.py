#Ejercicio con multiples excepciones

from math import factorial

def calcula_fact(num):
    try:
        fact = factorial(num)
    except TypeError:
        print("Factorial no soporta el valor dado")
    except ValueError:
        print("El factorial solo acepta numeros enteros positivos")
    else:
        print("El factorial de {} es {}".format(num, fact))

def numeros():
    Lista_num = [10, -5, 12, 'Azul']
    for n in Lista_num:
        calcula_fact(n)

numeros()        
        
        
