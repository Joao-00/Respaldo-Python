#ejercicio calculo del factorial de manera recursiva

#N! = N * N-1 * N-2 * N-3 * ... * N-N+1
#5! = 5 * 4 * 3 * 2 * 1


def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)


def principal():
    Num = int(input("Introduzca un numero entero positivo: "))
    if Num < 0:
        print("El numero debe ser positivo")
    else:
        print("El factorial del numero {} es {}".format(Num,factorial(Num)))

principal()



#ejercicio 2 sumar difitos de un numero de manera recursiva


def suma_digitos(Numero):
    if Numero == 0:
        return 0
    else:
        digito = Numero % 10
        return digito + suma_digitos(Numero // 10)

def Principal():
    Numero = int(input("Ingrese un numero: "))
    if Numero < -9 or Numero > 9:
        print("La suma de los digitos del {} es {}".format(Numero, suma_digitos(abs(Numero))))
    else:
        print("El numero es de un solo digito ", str(Numero))

Principal()
        
